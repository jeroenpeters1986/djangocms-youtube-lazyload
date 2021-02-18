#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
import django
django.setup()

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
    'AUTH_USER_MODEL': 'auth.User',
    'LANGUAGE_CODE': 'en',
    'SECRET_KEY': 'sfosaidfn9sfu90asunf9saunfisunfoiunfsadf',
}


def run():
    from app_helper import runner
    runner.cms('djangocms_youtube_lazyload')


if __name__ == '__main__':
    run()