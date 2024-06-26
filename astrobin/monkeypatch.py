# http://stackoverflow.com/questions/5877497/storing-images-and-thumbnails-on-s3-in-django
import json
import logging
import os
import subprocess
import tempfile
from numbers import Number
from os.path import splitext

from django.conf import settings
from django.core.files.images import ImageFile, get_image_dimensions
from moviepy.editor import VideoFileClip

logger = logging.getLogger(__name__)


def _get_video_dimensions(file_or_path):
    def get_video_rotation(path):
        cmd = [
            'ffprobe',
            '-v', 'error',
            '-select_streams', 'v:0',
            '-show_entries', 'stream_tags=rotate',
            '-of', 'json',
            path
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        metadata = json.loads(result.stdout.decode('utf-8'))
        return int(metadata['streams'][0]['tags'].get('rotate', '0'))

    if hasattr(file_or_path, 'read'):
        file = file_or_path
        file.seek(0)
    else:
        file = open(file_or_path, 'rb')

    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(file.read())
        temp_path = temp.name

    clip = VideoFileClip(temp_path)
    width, height = clip.size
    clip.close()

    rotation = get_video_rotation(temp_path)
    if rotation == 90 or rotation == 270:
        width, height = height, width

    os.unlink(temp_path)

    return width, height


def _get_image_dimensions(self):
    try:
        ext = splitext(self.file.name)[1].lower()
    except FileNotFoundError:
        return 0, 0

    if ext in settings.ALLOWED_VIDEO_EXTENSIONS:
        return _get_video_dimensions(self)

    if not hasattr(self, '_dimensions_cache'):
        close = self.closed

        if self.field.width_field and self.field.height_field:
            width = getattr(self.instance, self.field.width_field)
            height = getattr(self.instance, self.field.height_field)

            # Check if the fields have proper values.
            if isinstance(width, Number) and isinstance(height, Number) and width > 0 and height > 0:
                self._dimensions_cache = (width, height)
            else:
                try:
                    self.open()
                    self._dimensions_cache = get_image_dimensions(self, close=close)
                except Exception as e:
                    logger.error("_get_image_dimensions: %s" % str(e))
                    self._dimensions_cache = 0, 0
        else:
            try:
                self.open()
                self._dimensions_cache = get_image_dimensions(self, close=close)
            except Exception as e:
                logger.error("_get_image_dimensions: %s" % str(e))
                self._dimensions_cache = 0, 0

    if self._dimensions_cache[0] == 0 or self._dimensions_cache[1] == 0:
        logger.error("_get_image_dimensions: got 0 width or height")

    return self._dimensions_cache


ImageFile._get_image_dimensions = _get_image_dimensions
