import operator

from django.db.models import Q
from django_filters import rest_framework as filters

from astrobin.models import Image
from astrobin_apps_platesolving.models import Solution
from common.filters.list_filter import ListFilter
from functools import reduce


def filter_image_object_id(queryset, name, value):
    if not value.isdigit():
        # convert hash to image id
        try:
            image = Image.all_objects.get(hash=value)
            value = image.pk
        except Image.DoesNotExist:
            return Solution.objects.none()

    lookups = [name]

    or_queries = []

    try:
        search_terms = value.split()
    except AttributeError:
        search_terms = [value]

    for search_term in search_terms:
        or_queries += [Q(**{lookup: search_term}) for lookup in lookups]

    return queryset.filter(reduce(operator.or_, or_queries))


class SolutionListFilter(filters.FilterSet):
    object_id = filters.CharFilter(method=filter_image_object_id, field_name='object_id')
    object_ids = ListFilter(field_name='object_id', lookup_expr='in')

    class Meta:
        model = Solution
        fields = [
            'object_id',
            'content_type'
        ]
