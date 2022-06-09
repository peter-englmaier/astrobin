# noinspection PyMethodMayBeStatic

from typing import Dict, List, Union

from django.core.cache import cache
from django.db.models import QuerySet
from haystack import fields
from haystack.constants import Indexable
from haystack.indexes import SearchIndex

from astrobin.models import Image

PREPARED_FIELD_CACHE_EXPIRATION = 60
PREPARED_IMAGES_CACHE_KEY = 'astrobin_apps_equipment_search_indexed_images_%s_%d'

class EquipmentItemIndex(SearchIndex, Indexable):
    text = fields.CharField(document=True, use_template=True)

    # Top 10 users (by AstroBin Index) who have this item in at least one of their public images.
    users = fields.MultiValueField()

    # Number of users who have used this item.
    user_count = fields.IntegerField()

    # Top 50 images (by likes) that feature this item.
    images = fields.MultiValueField()

    # Number of images that feature this item.
    image_count = fields.IntegerField()

    def image_queryset(self, obj):
        raise NotImplemented

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def _prepare_images_cache(self, obj) -> List[Image]:
        images: List[Image] = cache.get(PREPARED_IMAGES_CACHE_KEY % (obj.__class__.__name__, obj.pk))
        images_and_likes: List[Dict[str, Union[Image, int]]] = []
        if images is None:
            qs: QuerySet = Image.objects.filter(self.image_queryset(obj))
            count: int = qs.count()
            image: Image

            if count > 0:
                for image in qs.iterator():
                    likes: int = image.likes()
                    images_and_likes.append(dict(image=image, likes=likes))

            images_and_likes = sorted(images_and_likes, key=lambda x: x.get('likes'), reverse=True)
            images = [x.get('image') for x in images_and_likes]
            cache.set(
                PREPARED_IMAGES_CACHE_KEY % (obj.__class__.__name__, obj.pk),
                images,
                PREPARED_FIELD_CACHE_EXPIRATION
            )
        return images

    def prepare_users(self, obj) -> List[int]:
        images: List[Image] = self._prepare_images_cache(obj)
        return list(set([x.user.pk for x in images]))[:10]

    def prepare_user_count(self, obj) -> int:
        images: List[Image] = self._prepare_images_cache(obj)
        count = len(set([x.user for x in images]))
        self.get_model().objects.filter(pk=obj.pk).update(user_count=count)
        return count

    def prepare_images(self, obj) -> List[int]:
        images: List[Image] = self._prepare_images_cache(obj)
        return list(set([x.pk for x in images]))[:50]

    def prepare_image_count(self, obj) -> int:
        images: List[Image] = self._prepare_images_cache(obj)
        count: int = len(images)
        self.get_model().objects.filter(pk=obj.pk).update(image_count=count)
        return count


    def get_updated_field(self):
        return 'last_added_or_removed_from_image'