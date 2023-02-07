import time
from datetime import timedelta

import mock
from django.test import TestCase, override_settings
from django.utils import timezone
from mock import patch

from astrobin.models import Image
from astrobin.signals import imagerevision_post_save
from astrobin.tests.generators import Generators
from astrobin_apps_equipment.tests.equipment_generators import EquipmentGenerators
from astrobin_apps_groups.models import Group
from toggleproperties.models import ToggleProperty


class SignalsTest(TestCase):

    @patch("astrobin.signals.push_notification")
    @patch("astrobin.signals.add_story")
    def test_imagerevision_post_save_wip_no_notifications(self, add_story, push_notification):
        revision = Generators.imageRevision()
        revision.image.is_wip = True

        push_notification.reset_mock()
        add_story.reset_mock()

        imagerevision_post_save(None, revision, True)

        self.assertFalse(push_notification.called)
        self.assertFalse(add_story.called)

    @patch("astrobin.signals.push_notification")
    @patch("astrobin.signals.add_story")
    def test_imagerevision_post_save_not_created_no_notifications(self, add_story, push_notification):
        revision = Generators.imageRevision()

        push_notification.reset_mock()
        add_story.reset_mock()

        imagerevision_post_save(None, revision, False)

        self.assertFalse(push_notification.called)
        self.assertFalse(add_story.called)

    @patch("astrobin.signals.push_notification")
    @patch("astrobin.signals.add_story")
    def test_imagerevision_post_save_skip_notifications(self, add_story, push_notification):
        revision = Generators.imageRevision()
        revision.skip_notifications = True

        push_notification.reset_mock()
        add_story.reset_mock()

        imagerevision_post_save(None, revision, True)

        self.assertFalse(push_notification.called)
        self.assertFalse(add_story.called)

    @patch("astrobin.signals.push_notification")
    @patch("astrobin.signals.add_story")
    def test_imagerevision_post_save_uploading(self, add_story, push_notification):
        revision = Generators.imageRevision()
        revision.uploader_in_progress = True

        push_notification.reset_mock()
        add_story.reset_mock()

        imagerevision_post_save(None, revision, True)

        self.assertFalse(push_notification.called)
        self.assertFalse(add_story.called)

    @patch("astrobin.signals.add_story")
    def test_imagerevision_post_save(self, add_story):
        revision = Generators.imageRevision()

        add_story.reset_mock()

        imagerevision_post_save(None, revision, True)

        self.assertTrue(add_story.called)

    def test_imaging_telescope_change_causes_image_to_be_saved(self):
        image = Generators.image()
        telescope = Generators.telescope()

        before = image.updated
        time.sleep(0.01)

        image.imaging_telescopes.add(telescope)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    def test_guiding_telescope_change_causes_image_to_be_saved(self):
        image = Generators.image()
        telescope = Generators.telescope()

        before = image.updated
        time.sleep(0.01)

        image.guiding_telescopes.add(telescope)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    def test_imaging_camera_change_causes_image_to_be_saved(self):
        image = Generators.image()
        camera = Generators.camera()

        before = image.updated
        time.sleep(0.01)

        image.imaging_cameras.add(camera)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    def test_guiding_camera_change_causes_image_to_be_saved(self):
        image = Generators.image()
        camera = Generators.camera()

        before = image.updated
        time.sleep(0.01)

        image.guiding_cameras.add(camera)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    def test_mount_change_causes_image_to_be_saved(self):
        image = Generators.image()
        mount = Generators.mount()

        before = image.updated
        time.sleep(0.01)

        image.mounts.add(mount)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    def test_filter_change_causes_image_to_be_saved(self):
        image = Generators.image()
        filter = Generators.filter()

        before = image.updated
        time.sleep(0.01)

        image.filters.add(filter)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    def test_focal_reducer_change_causes_image_to_be_saved(self):
        image = Generators.image()
        focal_reducer = Generators.focal_reducer()

        before = image.updated
        time.sleep(0.01)

        image.focal_reducers.add(focal_reducer)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    def test_accessory_change_causes_image_to_be_saved(self):
        image = Generators.image()
        accessory = Generators.accessory()

        before = image.updated
        time.sleep(0.01)

        image.accessories.add(accessory)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    def test_software_change_causes_image_to_be_saved(self):
        image = Generators.image()
        software = Generators.software()

        before = image.updated
        time.sleep(0.01)

        image.software.add(software)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    def test_imaging_telescope_2_change_causes_image_to_be_saved(self):
        image = Generators.image()
        telescope = EquipmentGenerators.telescope()

        Image.objects.filter(pk=image.pk).update(updated=timezone.now() - timedelta(minutes=1))
        image.refresh_from_db()

        before = image.updated
        time.sleep(0.01)

        image.imaging_telescopes_2.add(telescope)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    def test_guiding_telescope_2_change_causes_image_to_be_saved(self):
        image = Generators.image()
        telescope = EquipmentGenerators.telescope()

        Image.objects.filter(pk=image.pk).update(updated=timezone.now() - timedelta(minutes=1))
        image.refresh_from_db()

        before = image.updated
        time.sleep(0.01)

        image.guiding_telescopes_2.add(telescope)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    def test_imaging_camera_2_change_causes_image_to_be_saved(self):
        image = Generators.image()
        camera = EquipmentGenerators.camera()

        Image.objects.filter(pk=image.pk).update(updated=timezone.now() - timedelta(minutes=1))
        image.refresh_from_db()

        before = image.updated
        time.sleep(0.01)

        image.imaging_cameras_2.add(camera)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    def test_guiding_camera_2_change_causes_image_to_be_saved(self):
        image = Generators.image()
        camera = EquipmentGenerators.camera()

        Image.objects.filter(pk=image.pk).update(updated=timezone.now() - timedelta(minutes=1))
        image.refresh_from_db()

        before = image.updated
        time.sleep(0.01)

        image.guiding_cameras_2.add(camera)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    def test_mount_2_change_causes_image_to_be_saved(self):
        image = Generators.image()
        mount = EquipmentGenerators.mount()

        Image.objects.filter(pk=image.pk).update(updated=timezone.now() - timedelta(minutes=1))
        image.refresh_from_db()

        before = image.updated
        time.sleep(0.01)

        image.mounts_2.add(mount)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    def test_filter_2_change_causes_image_to_be_saved(self):
        image = Generators.image()
        filter = EquipmentGenerators.filter()

        Image.objects.filter(pk=image.pk).update(updated=timezone.now() - timedelta(minutes=1))
        image.refresh_from_db()

        before = image.updated
        time.sleep(0.01)

        image.filters_2.add(filter)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)


    def test_accessory_2_change_causes_image_to_be_saved(self):
        image = Generators.image()
        accessory = EquipmentGenerators.accessory()

        Image.objects.filter(pk=image.pk).update(updated=timezone.now() - timedelta(minutes=1))
        image.refresh_from_db()

        before = image.updated
        time.sleep(0.01)

        image.accessories_2.add(accessory)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    def test_software_2_change_causes_image_to_be_saved(self):
        image = Generators.image()
        software = EquipmentGenerators.software()

        Image.objects.filter(pk=image.pk).update(updated=timezone.now() - timedelta(minutes=1))
        image.refresh_from_db()

        before = image.updated
        time.sleep(0.01)

        image.software_2.add(software)

        image.refresh_from_db()

        self.assertGreater(image.updated, before)

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    @mock.patch('astrobin.signals.push_notification')
    def test_like_notification(self, push_notification):
        image = Generators.image()
        user = Generators.user()

        ToggleProperty.objects.create(
            property_type='like',
            user=user,
            content_object=image
        )

        push_notification.assert_has_calls(
            [
                mock.call([image.user], user, 'new_like', mock.ANY),
            ]
        )

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    @mock.patch('astrobin.signals.push_notification')
    def test_like_notification_for_collaborators(self, push_notification):
        image = Generators.image()
        user = Generators.user()
        collaborator = Generators.user()

        image.collaborators.add(collaborator)

        ToggleProperty.objects.create(
            property_type='like',
            user=user,
            content_object=image
        )

        push_notification.assert_has_calls(
            [
                mock.call([image.user, collaborator], user, 'new_like', mock.ANY),
            ]
        )

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    @mock.patch('astrobin.signals.push_notification')
    def test_bookmark_notification(self, push_notification):
        image = Generators.image()
        user = Generators.user()

        ToggleProperty.objects.create(
            property_type='bookmark',
            user=user,
            content_object=image
        )

        push_notification.assert_has_calls(
            [
                mock.call([image.user], user, 'new_bookmark', mock.ANY),
            ]
        )

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    @mock.patch('astrobin.signals.push_notification')
    def test_bookmark_notification_for_collaborators(self, push_notification):
        image = Generators.image()
        user = Generators.user()
        collaborator = Generators.user()

        image.collaborators.add(collaborator)

        ToggleProperty.objects.create(
            property_type='bookmark',
            user=user,
            content_object=image
        )

        push_notification.assert_has_calls(
            [
                mock.call([image.user, collaborator], user, 'new_bookmark', mock.ANY),
            ]
        )

    @mock.patch('astrobin.signals.push_notification')
    def test_image_collaborators_changed_sends_added_notification(self, push_notification):
        image = Generators.image()
        collaborator1 = Generators.user()
        collaborator2 = Generators.user()

        image.collaborators.add(collaborator1, collaborator2)

        push_notification.assert_has_calls(
            [
                mock.call(
                    [collaborator1, collaborator2], image.user, 'added_as_collaborator', mock.ANY
                ),
            ]
        )

        push_notification.reset_mock()

        # Adding a second time without removing doesn't send the notification again.

        image.collaborators.add(collaborator1, collaborator2)

        with self.assertRaises(AssertionError):
            push_notification.assert_has_calls(
                [
                    mock.call(
                        [collaborator1, collaborator2], image.user, 'added_as_collaborator', mock.ANY
                    ),
                ]
            )

    @mock.patch('astrobin.signals.push_notification')
    def test_image_collaborators_changed_sends_removed_notification(self, push_notification):
        image = Generators.image()
        collaborator1 = Generators.user()
        collaborator2 = Generators.user()

        image.collaborators.add(collaborator1, collaborator2)

        image.collaborators.remove(collaborator2)

        push_notification.assert_has_calls(
            [
                mock.call(
                    [collaborator2], image.user, 'removed_as_collaborator', mock.ANY
                ),
            ]
        )

    @mock.patch('astrobin.signals.push_notification')
    @mock.patch('astrobin.signals.UserService.clear_gallery_image_list_cache')
    def test_image_collaborators_changed_clears_gallery_cache(self, clear_gallery_image_list_cache, push_notification):
        image = Generators.image()
        collaborator1 = Generators.user()
        collaborator2 = Generators.user()

        # First reset because this was called when generating the image in the first place.
        clear_gallery_image_list_cache.reset_mock()

        self.assertFalse(clear_gallery_image_list_cache.called)
        image.collaborators.add(collaborator1, collaborator2)
        self.assertTrue(clear_gallery_image_list_cache.called)
        self.assertEquals(2, clear_gallery_image_list_cache.call_count)

        clear_gallery_image_list_cache.reset_mock()

        self.assertFalse(clear_gallery_image_list_cache.called)
        image.collaborators.remove(collaborator2)
        self.assertTrue(clear_gallery_image_list_cache.called)
        self.assertEquals(1, clear_gallery_image_list_cache.call_count)

    @mock.patch('astrobin.signals.push_notification')
    def test_user_joined_public_group_notification(self, push_notification):
        user = Generators.user()
        owner = Generators.user()
        group = Group.objects.create(
            name='test',
            creator=owner,
            owner=owner,
            public=True,
        )

        group.members.add(user)

        push_notification.assert_has_calls(
            [
                mock.call(
                    [owner], user, 'user_joined_public_group', mock.ANY
                ),
            ]
        )

    @mock.patch('astrobin.signals.push_notification')
    def test_user_joined_public_group_notification_creator(self, push_notification):
        user = Generators.user()
        creator = Generators.user()
        owner = Generators.user()
        group = Group.objects.create(
            name='test',
            creator=creator,
            owner=owner,
            public=True,
        )

        group.members.add(user)

        push_notification.assert_has_calls(
            [
                mock.call(
                    [owner], user, 'user_joined_public_group', mock.ANY
                ),
            ],
        )

    @mock.patch('astrobin.signals.push_notification')
    def test_user_joined_public_group_notification_when_owner_follows(self, push_notification):
        user = Generators.user()
        owner = Generators.user()

        ToggleProperty.objects.create(
            property_type='follow',
            user=owner,
            content_object=user

        )

        group = Group.objects.create(
            name='test',
            creator=owner,
            owner=owner,
            public=True,
        )

        group.members.add(user)

        push_notification.assert_has_calls(
            [
                mock.call(
                    [owner], user, 'user_joined_public_group', mock.ANY
                ),
            ]
        )

    @mock.patch('astrobin.signals.push_notification')
    def test_user_joined_public_group_notification_no_double_notification_for_member_and_owner(self, push_notification):
        user = Generators.user()
        owner = Generators.user()

        group = Group.objects.create(
            name='test',
            creator=owner,
            owner=owner,
            public=True,
        )

        group.members.add(owner)

        push_notification.reset_mock()

        group.members.add(user)

        push_notification.assert_has_calls(
            [
                mock.call(
                    [owner], user, 'user_joined_public_group', mock.ANY
                ),
            ]
        )
