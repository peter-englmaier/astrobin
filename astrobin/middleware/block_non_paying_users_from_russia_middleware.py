from django.http import HttpResponseBadRequest
from django.shortcuts import redirect

from astrobin.middleware.mixins import MiddlewareParentClass
from astrobin.utils import get_client_country_code
from astrobin_apps_premium.services.premium_service import PremiumService
from astrobin_apps_premium.templatetags.astrobin_apps_premium_tags import is_free


class BlockNonPayingUsersFromRussiaMiddleware(MiddlewareParentClass):
    def _process(self, request):
        is_localhost = 'localhost' in request.get_host() or '127.0.0.1' in request.get_host()

        if is_localhost:
            return False

        if not hasattr(request, 'user'):
            return False

        excluded_paths = [
            '/account',
            '/accounts',
            '/json-api/',
            '/thumb/',
            '/rawthumb/',
        ]


        for excluded_path in excluded_paths:
            if excluded_path in request.path:
                return False

        country_code = get_client_country_code(request)

        if country_code != 'ru':
            return False

        if request.user.is_authenticated and not is_free(PremiumService(request.user).get_valid_usersubscription()):
            return False

        return True

    def process_response(self, request, response):
        if self._process(request):
            url: str = 'https://welcome.astrobin.com/astrobin-stands-with-ukraine'

            if 'HTTP_AUTHORIZATION' in request.META:
                return HttpResponseBadRequest(f'AstroBin stands with Ukraine. Please see {url}')

            return redirect(url)

        return response
