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
    version=version,
    description="""YouTube video embed plugin for Django CMS. It uses
        lazyload embedding, so it's sitespeed impact is minimal""",
    long_description=readme,
    author='Jeroen Peters',
    author_email='jeroenpeters1986@gmail.com',
    url='https://github.com/jeroenpeters1986/djangocms-youtube-lazyload',
    packages=[
        'djangocms_youtube_lazyload',
    ],
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
    keywords='djangocms-youtube-lazyload, YouTube, django-cms, youtube embed, '
             'video embedding, cmsplugin, lazyload, cmsplugin-youtube, '
             'djangocms-youtube, sitespeed',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
