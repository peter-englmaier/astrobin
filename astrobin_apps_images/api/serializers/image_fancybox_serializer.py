from django.urls import reverse
from rest_framework import serializers

from astrobin.models import Image
from astrobin_apps_images.services import ImageService
from common.templatetags.common_tags import get_mime_type


class ImageFancyboxSerializer(serializers.ModelSerializer):
    hash = serializers.PrimaryKeyRelatedField(read_only=True)

    def to_representation(self, instance: Image):
        representation = super().to_representation(instance)
        final_revision = ImageService(instance).get_final_revision()

        representation.update({
            'url': instance.get_absolute_url(),
            'src': reverse('image_rawthumb', kwargs={'id': instance.get_id(), 'r': 'final', 'alias': 'qhd'}) + '?sync',
            'thumb': reverse(
                'image_rawthumb', kwargs={'id': instance.get_id(), 'r': 'final', 'alias': 'gallery'}
            ) + '?sync',
            'caption': f'{instance.user.userprofile.get_display_name()} - "{instance.title}"',
            'slug': instance.get_id(),
            'userId': instance.user.pk,
            'finalRevisionLabel': '0' if final_revision == instance else final_revision.label,
            'finalRevisionId': None if final_revision == instance else final_revision.id,
        })

        if (
                final_revision.video_file.name and
                final_revision.video_file.url and
                final_revision.encoded_video_file.name and
                final_revision.encoded_video_file.url
        ):
            representation.update({
                'videoUrl': final_revision.video_file.url,
                'encodedVideoUrl': final_revision.encoded_video_file.url,
                'videoFormat': get_mime_type(final_revision.video_file.url),
                'loopVideo': final_revision.loop_video,
            })

        return representation

    class Meta:
        model = Image
        fields = (
            'user',
            'pk',
            'hash',
            'title',
        )
