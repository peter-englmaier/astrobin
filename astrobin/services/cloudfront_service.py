import logging
import random
import string
import time
from typing import List

import boto3
import requests
from django.conf import settings

from astrobin.utils import extract_path_from_url

log = logging.getLogger(__name__)


class CloudFrontService:
    def __init__(self, distribution_id: str):
        self.distribution_id = distribution_id
        self.client = boto3.client('cloudfront')

    @staticmethod
    def generate_unique_reference():
        timestamp = str(time.time()).replace('.', '')  # Get the current timestamp without decimals
        random_string = ''.join(
            random.choices(string.ascii_letters + string.digits, k=6)
        )  # Generate a random string
        return timestamp + random_string

    def create_invalidation(self, urls: List[str]):
        if not self.distribution_id:
            return

        # Attempt to get the file. If it's missing, there's no need to invalidate it.
        for url in urls:
            log.debug("CloudFrontService checking if file exists: %s", url)
            try:
                if not url.startswith('http'):
                    url = f"{settings.MEDIA_URL}{url}"
                response = requests.get(url, timeout=5)
                if response.status_code != 200:
                    log.warning("CloudFrontService file %s does not exist" % url)
                    urls.remove(url)
            except Exception as e:
                log.warning("CloudFrontService unable to get file %s: %s" % (url, str(e)))
                urls.remove(url)

        if not urls or len(urls) == 0:
            log.warning("CloudFrontService cannot purge cache without urls")
            return

        log.debug("CloudFrontService purging cache for urls: %s", ', '.join(urls))

        return self.client.create_invalidation(
            DistributionId=self.distribution_id,
            InvalidationBatch={
                'Paths': {
                    'Quantity': len(urls),
                    'Items': [extract_path_from_url(x) for x in urls],
                },
                'CallerReference': self.generate_unique_reference()
            }
        )
