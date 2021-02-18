#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import djangocms_youtube_lazyload

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangocms_youtube_lazyload.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.md').read()

setup(
    name='djangocms-youtube-lazyload',
    packages=[
        'djangocms_youtube_lazyload',
    ],
    version=version,
    description='DjangoCMS YouTube video embed plugin with minimal impact',
    long_description_content_type='text/markdown',
    long_description=readme,
    licence='MIT',
    author='Jeroen Peters',
    author_email='jeroenpeters1986@gmail.com',
    url='https://github.com/jeroenpeters1986/djangocms-youtube-lazyload',
    include_package_data=True,
    install_requires=[
        'django-appconf',
        'django-cms>=3.0',
        'isodate>=0.5.4',
        'jsonfield>=2.1.1',
        'requests',
    ],
    license="BSD",
    zip_safe=False,
    test_suite='tests.settings.test',
    keywords='djangocms-youtube-lazyload, YouTube, django-cms, youtube embed, '
             'video embedding, cmsplugin, lazyload, cmsplugin-youtube, '
             'djangocms-youtube, sitespeed',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
    ],
)
