from distutils.version import LooseVersion

from django import VERSION as DJANGO_VERSION

import cms
from cms.api import add_plugin, create_page
from cms.test_utils.testcases import CMSTestCase

from djangocms_youtube_lazyload.models import YoutubeLazyload

DJANGO_111 = DJANGO_VERSION[:2] >= (1, 11)
CMS_3_6 = LooseVersion(cms.__version__) < LooseVersion('4.0')


class YoutubeLazyloadPluginTestCase(CMSTestCase):
    def setUp(self):
        super(YoutubeLazyloadPluginTestCase, self).setUp()

        self.page = create_page('test page', 'test_page.html', 'en', published=True)
        try:
            self.placeholder = self.page.placeholders.get(slot='content')
        except AttributeError:
            self.placeholder = self.page.get_placeholders('en').get(slot='content')

        plugin_data = {
            'title': 'K3',
            'video_url': 'https://www.youtube.com/watch?v=BckqHBqFgQQ',
            'description': 'De Kwis',
            'theme': 'dark',
            'plugin_template': 'djangocms_youtube_lazyload/video.html',
            'video_data': '{status":{"license":"youtube","embeddable":true,"privacyStatus":"public","publicStatsViewable":true,"madeForKids":false,"uploadStatus":"processed"},"kind":"youtube#video","contentDetails":{"definition":"sd","projection":"rectangular","contentRating":{},"caption":"true","duration":"PT3M4S","licensedContent":true,"dimension":"2d"},"snippet":{"description":"Meer zien? Ga naar http://dekwis.vara.nl","title":"De Kwis - K3","channelId":"UCX0jEflGtoRIe1Gi5QHFFrQ","publishedAt":"2015-03-21T19:57:40Z","liveBroadcastContent":"none","tags":["K3","De Kwis"],"channelTitle":"Even tot hier","thumbnails":{"default":{"url":"https://i.ytimg.com/vi/eUFv9HiPjBE/default.jpg","width":120,"height":90},"high":{"url":"https://i.ytimg.com/vi/eUFv9HiPjBE/hqdefault.jpg","width":480,"height":360},"medium":{"url":"https://i.ytimg.com/vi/eUFv9HiPjBE/mqdefault.jpg","width":320,"height":180},"maxres":{"url":"https://i.ytimg.com/vi/eUFv9HiPjBE/maxresdefault.jpg","width":1280,"height":720},"standard":{"url":"https://i.ytimg.com/vi/eUFv9HiPjBE/sddefault.jpg","width":640,"height":480}},"categoryId":"23","localized":{"description":"Meer zien? Ga naar http://dekwis.vara.nl","title":"De Kwis - K3"},"categoryName":"Comedy"},"player":{"embedHtml":"<iframe width=\"480\" height=\"270\" src=\"//www.youtube.com/embed/eUFv9HiPjBE\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>"},"etag":"CIKIAxbtuaGA4AJN5o5ktFyFVJE","id":"eUFv9HiPjBE"}',
        }
        self.video_plugin = add_plugin(self.placeholder, 'YoutubeLazyloadPlugin', 'en', **plugin_data)

    def test_form_submission_default_action(self):
        self.video_plugin.save()
        if CMS_3_6:
            self.page.publish('en')

        response = self.client.post(self.page.get_absolute_url('en'), {})

        self.assertEquals(response.status_code, 200)
        self.assertEquals(YoutubeLazyload.objects.count(), 1)
