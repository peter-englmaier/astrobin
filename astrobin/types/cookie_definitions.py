from django.conf import settings
from django.utils.translation import gettext_lazy as _

cookie_definitions = {
    'astrobin_cookie_consent': _(
        'This cookie is used to store your cookie preferences.'
    ),
    'sessionid': _(
        'This cookie is used to identify your session on the website.'
    ),
    'csrftoken': _(
        'This cookie is used to protect against Cross-Site Request Forgery (CSRF) attacks.'
    ),
    'astrobin_lang': _(
        'This cookie is used to remember your language preference.'
    ),
    'astrobin-two-factor-remember-cookie': _(
        'This cookie lets you skip the two-factor authentication step for a certain time on the current device.'
    ),
    'astrobin-equipment-explorer-filter-data-camera': _(
        'This cookie is used to remember your last camera filter in the equipment explorer.'
    ),
    'astrobin-equipment-explorer-filter-data-sensor': _(
        'This cookie is used to remember your last sensor filter in the equipment explorer.'
    ),
    'astrobin-equipment-explorer-filter-data-telescope': _(
        'This cookie is used to remember your last telescope filter in the equipment explorer.'
    ),
    'astrobin-equipment-explorer-filter-data-mount': _(
        'This cookie is used to remember your last mount filter in the equipment explorer.'
    ),
    'astrobin-equipment-explorer-filter-data-filter': _(
        'This cookie is used to remember your last filter filter in the equipment explorer.'
    ),
    'astrobin-equipment-explorer-filter-data-software': _(
        'This cookie is used to remember your last software filter in the equipment explorer.'
    ),
    'astrobin-equipment-explorer-filter-data-accessory': _(
        'This cookie is used to remember your last accessory filter in the equipment explorer.'
    ),
    'multidb_pin_writes': _(
        'This cookie is used to pin your session to the master database: AstroBin uses multiple databases to improve '
        'performance, and this cookie is used to make sure that all your requests are sent to the same database.'
    ),
    'classic-auth-token': _(
        'This cookie is used to authenticate you on the website app.astrobin.com.'
    ),
    '__stripe_mid': _(
        'This cookie is set by Stripe and used for fraud prevention. It is only set if you purchase a subscription.'
    ),
    '__stripe_sid': _(
        'This cookie is set by Stripe and used for fraud prevention. It is only set if you purchase a subscription.'
    ),
    'astrobin_forum_usage_modal_seen': _(
        'This cookie is used to remember if you have seen the information about proper usage of the forums.'
    ),
    'astrobin_click_and_drag_toast_seen': _(
        'This cookie is used to remember if you have seen information about the click & drag zoom functionality.'
    ),
    'astrobin_use_high_contrast_theme': _(
        'This cookie is used to remember if you have enabled the high contrast theme.'
    ),
    'astrobin_last_seen_set': _(
        'This cookie is used avoid saving the date and time we last saw you too often.'
    ),
    '_ga': _(
        'This cookie is used by Google Analytics to anonymously track your usage of the website.'
    ),
    '_gid': _(
        'This cookie is used by Google Analytics to anonymously track your usage of the website.'
    ),
    '_gat': _(
        'This cookie is used by Google Analytics to anonymously track your usage of the website.'
    ),
    f'_gac_{settings.GOOGLE_ANALYTICS_ID}': _(
        'This cookie is used by Google Analytics to anonymously track your usage of the website.'
    ),
    'IDE': _(
        'This cookie is used by Google Ad Manager to register and report the website user\'s actions after viewing or '
        'clicking one of the advertiser\'s ads with the purpose of measuring the efficacy of an ad.'
    ),
    'test_cookie': _('This cookie is used by Google Ad Manager to check if the user\'s browser supports cookies.'),
}
