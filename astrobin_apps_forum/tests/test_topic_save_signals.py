from datetime import timedelta

from django.test import TestCase
import mock
from django.utils import timezone

from astrobin.tests.generators import Generators
from astrobin_apps_equipment.models.equipment_item import EquipmentItemReviewerDecision
from astrobin_apps_equipment.tests.equipment_generators import EquipmentGenerators


class TestTopicSaveSignals(TestCase):
    @mock.patch('astrobin_apps_forum.services.forum_service.push_notification')
    def test_notification_for_equipment_item_topics(self, push_notification):
        user1 = Generators.user()
        user2 = Generators.user()

        image1 = Generators.image(user=user1)
        Generators.image(user=user2)

        telescope = EquipmentGenerators.telescope(reviewer_decision=EquipmentItemReviewerDecision.APPROVED)
        image1.imaging_telescopes_2.add(telescope)

        forum = telescope.forum

        self.assertIsNotNone(forum)

        topic = Generators.forum_topic(forum=forum)

        push_notification.assert_has_calls(
            [
                mock.call([user1], topic.user, 'new_topic_for_equipment_you_use', mock.ANY),
            ], any_order=True
        )

    @mock.patch('astrobin_apps_forum.services.forum_service.push_notification')
    def test_notification_for_equipment_item_topics_for_users_of_variants(self, push_notification):
        user1 = Generators.user()
        user2 = Generators.user()

        image1 = Generators.image(user=user1)
        image2 = Generators.image(user=user2)

        telescope = EquipmentGenerators.telescope(reviewer_decision=EquipmentItemReviewerDecision.APPROVED)
        variant = EquipmentGenerators.telescope(reviewer_decision=EquipmentItemReviewerDecision.APPROVED, variant_of=telescope, brand=telescope.brand)

        image1.imaging_telescopes_2.add(telescope)
        image2.imaging_telescopes_2.add(variant)

        forum = telescope.forum

        topic = Generators.forum_topic(forum=forum)

        push_notification.assert_has_calls(
            [
                mock.call([user1, user2], topic.user, 'new_topic_for_equipment_you_use', mock.ANY),
            ], any_order=True
        )

    @mock.patch('astrobin_apps_forum.services.forum_service.push_notification')
    def test_notification_for_equipment_item_topics_for_users_of_variants_reverse(self, push_notification):
        user1 = Generators.user()
        user2 = Generators.user()

        image1 = Generators.image(user=user1)
        image2 = Generators.image(user=user2)

        telescope = EquipmentGenerators.telescope(reviewer_decision=EquipmentItemReviewerDecision.APPROVED)
        variant = EquipmentGenerators.telescope(
            reviewer_decision=EquipmentItemReviewerDecision.APPROVED, variant_of=telescope, brand=telescope.brand
        )

        image1.imaging_telescopes_2.add(telescope)
        image2.imaging_telescopes_2.add(variant)

        forum = variant.forum

        topic = Generators.forum_topic(forum=forum)

        push_notification.assert_has_calls(
            [
                mock.call([user1, user2], topic.user, 'new_topic_for_equipment_you_use', mock.ANY),
            ], any_order=True
        )

    @mock.patch('astrobin_apps_forum.services.forum_service.push_notification')
    def test_notification_for_equipment_item_topics_doesnt_send_to_post_user(self, push_notification):
        user = Generators.user()
        image = Generators.image(user=user)
        telescope = EquipmentGenerators.telescope(reviewer_decision=EquipmentItemReviewerDecision.APPROVED)
        image.imaging_telescopes_2.add(telescope)

        forum = telescope.forum
        Generators.forum_topic(forum=forum, user=user)

        with self.assertRaises(AssertionError):
            push_notification.assert_called_with(mock.ANY, user, 'new_topic_for_equipment_you_use', mock.ANY)

    @mock.patch('astrobin_apps_forum.services.forum_service.push_notification')
    def test_notification_for_equipment_item_topics_doesnt_send_if_on_moderation(self, push_notification):
        user = Generators.user()
        image = Generators.image(user=user)
        telescope = EquipmentGenerators.telescope(reviewer_decision=EquipmentItemReviewerDecision.APPROVED)
        image.imaging_telescopes_2.add(telescope)

        forum = telescope.forum
        Generators.forum_topic(forum=forum, on_moderation=True)

        with self.assertRaises(AssertionError):
            push_notification.assert_called_with([user], mock.ANY, 'new_topic_for_equipment_you_use', mock.ANY)
    @mock.patch('astrobin_apps_forum.services.forum_service.push_notification')
    def test_notification_for_equipment_item_topics_doesnt_send_if_old_topic(self, push_notification):
        user1 = Generators.user()
        user2 = Generators.user()

        image1 = Generators.image(user=user1)
        Generators.image(user=user2)

        telescope = EquipmentGenerators.telescope(reviewer_decision=EquipmentItemReviewerDecision.APPROVED)
        image1.imaging_telescopes_2.add(telescope)

        forum = telescope.forum

        self.assertIsNotNone(forum)

        topic = Generators.forum_topic(forum=forum)
        push_notification.reset_mock()

        topic.created = timezone.now() - timedelta(days=7) - timedelta(seconds=1)
        topic.save()

        with self.assertRaises(AssertionError):
            push_notification.assert_called_with([user1], topic.user, 'new_topic_for_equipment_you_use', mock.ANY)

    @mock.patch('astrobin_apps_forum.services.forum_service.push_notification')
    def test_notification_for_topics_if_you_follow_equipment(self, push_notification):
        follower = Generators.user()
        poster = Generators.user()
        telescope = EquipmentGenerators.telescope(reviewer_decision=EquipmentItemReviewerDecision.APPROVED)
        Generators.follow(telescope, user=follower)

        forum = telescope.forum
        topic = Generators.forum_topic(forum=forum, user=poster)

        push_notification.assert_called_with([follower], topic.user, 'new_topic_for_equipment_you_follow', mock.ANY)

    @mock.patch('astrobin_apps_forum.services.forum_service.push_notification')
    def test_notification_for_topics_if_you_follow_equipment_except_users(self, push_notification):
        follower = Generators.user()
        poster = Generators.user()
        image = Generators.image(user=follower)
        telescope = EquipmentGenerators.telescope(reviewer_decision=EquipmentItemReviewerDecision.APPROVED)
        image.imaging_telescopes_2.add(telescope)
        Generators.follow(telescope, user=follower)

        forum = telescope.forum
        topic = Generators.forum_topic(forum=forum, user=poster)

        with self.assertRaises(AssertionError):
            push_notification.assert_called_with([follower], topic.user, 'new_topic_for_equipment_you_follow', mock.ANY)

