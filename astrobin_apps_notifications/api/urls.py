from django.conf.urls import url, include
from rest_framework import routers

from astrobin_apps_notifications.api.views import NotificationViewSet, NoticeSettingViewSet, NoticeTypeViewSet

router = routers.DefaultRouter()
router.register(r'notification', NotificationViewSet, basename='notification')
router.register(r'type', NoticeTypeViewSet, basename='type')
router.register(r'setting', NoticeSettingViewSet, basename='setting')

urlpatterns = [
    url('', include(router.urls)),
]
