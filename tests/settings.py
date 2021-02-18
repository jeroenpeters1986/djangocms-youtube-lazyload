#!/usr/bin/env python
from __future__ import division, print_function, unicode_literals


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
    'SECRET_KEY': 'sfosaidfn9sfu90asunf9saunfisunfoiunfsadf',
}


def run():
    from djangocms_helper import runner
    runner.cms('djangocms_youtube_lazyload')


if __name__ == '__main__':
    run()