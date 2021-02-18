#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gettext(s):
    return s


HELPER_SETTINGS = {
    'INSTALLED_APPS': [
        'tests',
        'djangocms_youtube_lazyload',
    ],
    'CMS_LANGUAGES': {
        1: [{
            'code': 'en',
            'name': 'English',
        }]
    },
    'CMS_TEMPLATES': (
        ('test_page.html', 'Normal page'),
    ),
    'LANGUAGE_CODE': 'en',
}


def test():
    from app_helper import runner
    runner.cms('djangocms_youtube_lazyload')


if __name__ == '__main__':
    test()