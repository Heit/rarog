from django.core.urlresolvers import reverse, NoReverceMatch
from django.newforms import HiddenInput, TextInput
from django.utils import simplejson
from django.utils.safestring import mark_safe


class AutoCompleteWidget(TextInput):
    def __init__(self, attrs=None, choises=None, choises_url=None, options=None, related_fields=None):
        self.attrs = attrs or {}
        self.choise, self.choises, self.choises_url = None, choises, choises_url
        self.options = options or {}

        if related_fields:
            extra = {}
            if isinstance(related_fields, str):
                related_fields = list(related_fields)

            for field in related_fields:
                extra[field] = "%s_value" %field

            self.extra = extra
        else:
            self.extra = {}
