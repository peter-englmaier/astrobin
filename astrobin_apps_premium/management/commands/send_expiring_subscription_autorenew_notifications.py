# Python
from datetime import datetime, timedelta

# Django
from django.conf import settings
from django.core.management.base import BaseCommand
from django.urls import reverse

# Third party
from subscription.models import UserSubscription

# AstroBin
from astrobin_apps_notifications.utils import push_notification
from astrobin_apps_premium.services.premium_service import SubscriptionName


class Command(BaseCommand):
    help = "Send a notification to user when their premium subscription " +\
           "auto-renews in one week."

    def handle(self, *args, **kwargs):
        user_subscriptions = UserSubscription.objects\
            .filter(
                subscription__name__in = [
                    SubscriptionName.LITE_CLASSIC_AUTORENEW.value,
                    SubscriptionName.LITE_2020_AUTORENEW_MONTHLY.value,
                    SubscriptionName.PREMIUM_CLASSIC_AUTORENEW.value,
                    SubscriptionName.PREMIUM_2020_AUTORENEW_MONTHLY.value,
                    SubscriptionName.ULTIMATE_2020_AUTORENEW_MONTHLY.value,
                ],
                cancelled=False,
                expires=datetime.now() + timedelta(days=7)
            )

        for user_subscription in user_subscriptions:
            push_notification([user_subscription.user], None, 'expiring_subscription_autorenew', {
                'user_subscription': user_subscription,
            })

        user_subscriptions = UserSubscription.objects \
            .filter(
            subscription__name__in=[
                SubscriptionName.LITE_CLASSIC_AUTORENEW.value,
                SubscriptionName.LITE_2020_AUTORENEW_YEARLY.value,
                SubscriptionName.PREMIUM_CLASSIC_AUTORENEW.value,
                SubscriptionName.PREMIUM_2020_AUTORENEW_YEARLY.value,
                SubscriptionName.ULTIMATE_2020_AUTORENEW_YEARLY.value,
            ],
            cancelled=False,
            expires=datetime.now() + timedelta(days=30)
        )

        for user_subscription in user_subscriptions:
            push_notification([user_subscription.user], None, 'expiring_subscription_autorenew_30d', {
                'user_subscription': user_subscription,
            })
