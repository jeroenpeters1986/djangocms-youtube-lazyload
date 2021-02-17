# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.urls import reverse

from .models import YoutubeLazyload


class YoutubeVideoURLWidget(forms.TextInput):
    model = YoutubeLazyload

    def render(self, name, value, attrs=None, renderer=None, **kwargs):
        if attrs is None:
            attrs = {}

        opts = self.model._meta

        app_label = opts.app_label
        model_name = opts.model_name

        attrs['data-gdata'] = reverse('admin:%s_%s_%s' % (app_label, model_name, 'gdata',))
        return super(YoutubeVideoURLWidget, self).render(name, value, attrs)
