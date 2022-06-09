from django.db.models import Q

from astrobin_apps_equipment.models import Mount
from astrobin_apps_equipment.search_indexes.equipment_item_index import EquipmentItemIndex


class MountIndex(EquipmentItemIndex):
    def get_model(self):
        return Mount

    # noinspection PyMethodMayBeStatic
    def image_queryset(self, obj: Mount) -> Q:
        return Q(mounts_2=obj)