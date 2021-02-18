# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.http import HttpResponseNotAllowed, JsonResponse
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .conf import settings
from .exceptions import YoutubeAPIError
from .forms import YoutubeLazyloadModelForm
from .models import YoutubeLazyload
from .utils import get_video_details


@plugin_pool.register_plugin
class YoutubeLazyloadPlugin(CMSPluginBase):
    model = YoutubeLazyload
    form = YoutubeLazyloadModelForm

    module = settings.DJANGOCMS_YOUTUBE_LAZYLOAD_PLUGIN_MODULE
    name = settings.DJANGOCMS_YOUTUBE_LAZYLOAD_PLUGIN_NAME
    render_template = 'djangocms_youtube_lazyload/video.html'

    text_enabled = settings.DJANGOCMS_YOUTUBE_LAZYLOAD_TEXT_ENABLED
    page_only = settings.DJANGOCMS_YOUTUBE_LAZYLOAD_PAGE_ONLY
    require_parent = settings.DJANGOCMS_YOUTUBE_LAZYLOAD_REQUIRE_PARENT
    parent_classes = settings.DJANGOCMS_YOUTUBE_LAZYLOAD_PARENT_CLASSES
    allow_children = settings.DJANGOCMS_YOUTUBE_LAZYLOAD_ALLOW_CHILDREN
    child_classes = settings.DJANGOCMS_YOUTUBE_LAZYLOAD_CHILD_CLASSES

    change_form_template = 'djangocms_youtube_lazyload/cms_youtube_change.html'

    def get_fieldsets(self, request, obj=None):
        if settings.DJANGOCMS_YOUTUBE_LAZYLOAD_FIELDSETS:
            return settings.DJANGOCMS_YOUTUBE_LAZYLOAD_FIELDSETS

        advanced_option_fields = ('theme', )
        if settings.DJANGOCMS_YOUTUBE_LAZYLOAD_ENABLE_CUSTOM_VIDEO_SIZE:
            advanced_option_fields += ('width', 'height', )

        fieldsets = (
            (None, {
                'fields': ('video_url', )
            }),
            (None, {
                'fields': ('title', 'description', 'description_option', )
            }),
            (None, {
                'fields': advanced_option_fields
            }),
            (None, {
                'fields': ('thumbnail',)
            }),
            (_('Video Meta'), {
                'classes': ('advanced', 'collapse'),
                'fields': ('video_data', ),
            }),
        )

        return fieldsets

    def get_model_info(self):
        return self.model._meta.app_label, self.model._meta.model_name

    def get_plugin_urls(self):
        from django.conf.urls import url
        info = self.get_model_info()

        return [
            url(r'^gdata/$',
                admin.site.admin_view(self.youtube_data_api),
                name='%s_%s_gdata' % info),
        ]

    def youtube_data_api(self, request):
        if not request.method == 'POST':
            return HttpResponseNotAllowed(['POST', ])

        video_id = request.POST.get('video_id', None)
        if video_id is None:
            response = {
                'status': 400,
                'error_type': 'idRequired',
                'error_message': '',
            }
            return JsonResponse(response, status=400)

        try:
            response = get_video_details(video_id)
        except YoutubeAPIError as e:
            response = {
                'status': e.status_code,
                'error_type': e.error_type,
                'error_message': e.error_message,
            }
            return JsonResponse(response, status=e.status_code)
        else:
            return JsonResponse(response)
