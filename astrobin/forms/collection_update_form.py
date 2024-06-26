from django import forms
from django.utils.translation import ugettext as _

from astrobin.forms.utils import NULL_CHOICE
from astrobin.models import Collection
from astrobin_apps_images.models import KeyValueTag


class CollectionUpdateForm(forms.ModelForm):
    error_css_class = 'error'

    order_by_tag = forms.ChoiceField(
        required=False,
        help_text=_("Select a tag to order this collection by its value. If you see no options here, it's because "
                    "none of the images in this collection have key/value tags. PS: Images that lack this tag will "
                    "appear at the bottom of the collection.")
    )

    def __init__(self, *args, **kwargs):
        super(CollectionUpdateForm, self).__init__(*args, **kwargs)

        tag_keys = KeyValueTag.objects \
            .filter(image__user=self.instance.user) \
            .distinct() \
            .values_list("key", flat=True)

        self.fields['order_by_tag'].choices = NULL_CHOICE + [(x, x) for x in tag_keys]
        self.fields['parent'].queryset = Collection.objects.filter(
            user=self.instance.user
        ).exclude(
            pk=self.instance.pk
        ).order_by(
            'name'
        )

    class Meta:
        model = Collection
        fields = ('name', 'description', 'parent', 'cover', 'order_by_tag')
