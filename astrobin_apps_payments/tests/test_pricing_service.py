from datetime import date, datetime, timedelta
from unittest.mock import patch

from django.contrib.auth.models import Group
from django.test import TestCase
from mock import PropertyMock
from subscription.models import Subscription

from astrobin.tests.generators import Generators
from astrobin_apps_payments.models import ExchangeRate
from astrobin_apps_payments.services.pricing_service import PricingService
from astrobin_apps_premium.services.premium_service import SubscriptionDisplayName, SubscriptionName


class PricingServiceTest(TestCase):
    def setUp(self):
        Subscription.objects.create(
            name=SubscriptionName.LITE_2020,
            price=20,
            group=Group.objects.create(name='astrobin_lite')
        )

        Subscription.objects.create(
            name=SubscriptionName.PREMIUM_2020,
            price=40,
            group=Group.objects.create(name='astrobin_premium')
        )

        Subscription.objects.create(
            name=SubscriptionName.ULTIMATE_2020,
            price=60,
            group=Group.objects.create(name='astrobin_ultimate')
        )

        ExchangeRate.objects.create(
            source='CHF',
            target='USD',
            rate=1.1,
            time=datetime.now()
        )

        ExchangeRate.objects.create(
            source='CHF',
            target='EUR',
            rate=1.101,
            time=datetime.now()
        )

    @patch('astrobin_apps_payments.services.pricing_service.PricingService.get_stripe_price')
    def test_chf(self, get_stripe_price):
        get_stripe_price.return_value = 20
        self.assertEqual(20, PricingService.get_price(SubscriptionDisplayName.LITE, 'CH', 'CHF'))

        get_stripe_price.return_value = 40
        self.assertEqual(40, PricingService.get_price(SubscriptionDisplayName.PREMIUM, 'CH', 'CHF'))

        get_stripe_price.return_value = 60
        self.assertEqual(60, PricingService.get_price(SubscriptionDisplayName.ULTIMATE, 'CH', 'CHF'))

    @patch('astrobin_apps_payments.services.pricing_service.PricingService.get_stripe_price')
    def test_usd(self, get_stripe_price):
        get_stripe_price.return_value = 22
        self.assertEqual(22.0, PricingService.get_price(SubscriptionDisplayName.LITE, 'US', 'USD'))

        get_stripe_price.return_value = 44
        self.assertEqual(44.0, PricingService.get_price(SubscriptionDisplayName.PREMIUM, 'US', 'USD'))

        get_stripe_price.return_value = 66
        self.assertEqual(66.0, PricingService.get_price(SubscriptionDisplayName.ULTIMATE, 'US', 'USD'))

    @patch('astrobin_apps_payments.services.pricing_service.PricingService.get_stripe_price')
    def test_eur_with_50c_rounding_up(self, get_stripe_price):
        get_stripe_price.return_value = 22.5
        self.assertEqual(22.5, PricingService.get_price(SubscriptionDisplayName.LITE, 'DE', 'EUR'))

        get_stripe_price.return_value = 44.5
        self.assertEqual(44.5, PricingService.get_price(SubscriptionDisplayName.PREMIUM, 'DE', 'EUR'))

        get_stripe_price.return_value = 66.5
        self.assertEqual(66.5, PricingService.get_price(SubscriptionDisplayName.ULTIMATE, 'DE', 'EUR'))

    def test_are_non_autorenewing_subscription_supported_when_user_is_None(self):
        self.assertFalse(PricingService.non_autorenewing_supported(None))

    def test_are_non_autorenewing_subscription_supported_when_user_is_not_authenticated(self):
        self.assertFalse(PricingService.non_autorenewing_supported(Generators.user()))

    @patch('django.contrib.auth.models.User.is_authenticated', new_callable=PropertyMock)
    def test_are_non_autorenewing_subscription_supported_when_user_does_not_have_any_subscriptions(
            self, is_authenticated
    ):
        is_authenticated.return_value = True

        self.assertFalse(PricingService.non_autorenewing_supported(Generators.user()))

    @patch('django.contrib.auth.models.User.is_authenticated', new_callable=PropertyMock)
    def test_are_non_autorenewing_subscription_supported_when_user_has_subscription_but_its_recurring(
            self, is_authenticated
    ):
        is_authenticated.return_value = True

        user = Generators.user()
        Generators.premium_subscription(user, SubscriptionName.LITE_CLASSIC_AUTORENEW)

        self.assertFalse(PricingService.non_autorenewing_supported(user))

    @patch('django.contrib.auth.models.User.is_authenticated', new_callable=PropertyMock)
    def test_are_non_autorenewing_subscription_supported_when_user_has_non_recurring_subscription_but_its_expired_too_long_ago(
            self, is_authenticated
    ):
        is_authenticated.return_value = True

        user = Generators.user()
        us = Generators.premium_subscription(user, SubscriptionName.LITE_CLASSIC_AUTORENEW)
        us.expires = date.today() - timedelta(365*2+1)
        us.save()

        self.assertFalse(PricingService.non_autorenewing_supported(user))

    @patch('django.contrib.auth.models.User.is_authenticated', new_callable=PropertyMock)
    def test_are_non_autorenewing_subscription_supported_when_user_has_non_recurring_subscription_not_expired_too_long_ago(
            self, is_authenticated
    ):
        is_authenticated.return_value = True

        user = Generators.user()
        us = Generators.premium_subscription(user, SubscriptionName.PREMIUM_2020)
        us.expires = date.today() - timedelta(365*2-1)
        us.save()

        self.assertTrue(PricingService.non_autorenewing_supported(user))

    @patch('django.contrib.auth.models.User.is_authenticated', new_callable=PropertyMock)
    def test_are_non_autorenewing_subscription_supported_when_user_has_non_recurring_subscription_not_expired_too_long_ago_but_recurring_subscription_too(
            self, is_authenticated
    ):
        is_authenticated.return_value = True

        user = Generators.user()

        us = Generators.premium_subscription(user, SubscriptionName.PREMIUM_2020)
        us.expires = date.today() - timedelta(365 * 2 - 1)
        us.save()

        us = Generators.premium_subscription(user, SubscriptionName.ULTIMATE_2020_AUTORENEW_YEARLY)
        us.expires = date.today() + timedelta(365)
        us.save()

        self.assertFalse(PricingService.non_autorenewing_supported(user))
