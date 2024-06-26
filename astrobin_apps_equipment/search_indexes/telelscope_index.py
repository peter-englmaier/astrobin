from django.db.models import Q
from haystack.constants import Indexable

from astrobin_apps_equipment.models import Telescope
from astrobin_apps_equipment.search_indexes.equipment_item_index import EquipmentItemIndex


class TelescopeIndex(EquipmentItemIndex, Indexable):
    def get_model(self):
        return Telescope

    # noinspection PyMethodMayBeStatic
    def image_queryset(self, obj: Telescope) -> Q:
        return Q(imaging_telescopes_2=obj) |\
               Q(guiding_telescopes_2=obj) |\
               Q(imaging_telescopes_2__in=obj.variants.all()) |\
               Q(guiding_telescopes_2__in=obj.variants.all())

    # noinspection PyMethodMayBeStatic
    def user_queryset(self, obj: Telescope) -> Q:
        return Q(image__imaging_telescopes_2=obj) | \
               Q(image__guiding_telescopes_2=obj) | \
               Q(image__imaging_telescopes_2__in=obj.variants.all()) | \
               Q(image__guiding_telescopes_2__in=obj.variants.all())
