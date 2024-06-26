from django.db.models import Q
from haystack.constants import Indexable

from astrobin_apps_equipment.models import Camera
from astrobin_apps_equipment.search_indexes.equipment_item_index import EquipmentItemIndex


class CameraIndex(EquipmentItemIndex, Indexable):
    def get_model(self):
        return Camera

    # noinspection PyMethodMayBeStatic
    def image_queryset(self, obj: Camera) -> Q:
        return Q(imaging_cameras_2=obj) |\
               Q(guiding_cameras_2=obj) |\
               Q(imaging_cameras_2__in=obj.variants.all()) |\
               Q(guiding_cameras_2__in=obj.variants.all())

    # noinspection PyMethodMayBeStatic
    def user_queryset(self, obj: Camera) -> Q:
        return Q(image__imaging_cameras_2=obj) | \
               Q(image__guiding_cameras_2=obj) | \
               Q(image__imaging_cameras_2__in=obj.variants.all()) | \
               Q(image__guiding_cameras_2__in=obj.variants.all())
