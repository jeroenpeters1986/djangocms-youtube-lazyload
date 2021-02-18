# -*- coding: utf-8 -*-
from django.core.management import call_command
from django.test import TestCase, override_settings

from six.moves import StringIO


class MigrationTestCase(TestCase):

    @override_settings(MIGRATION_MODULES={})
    def test_for_missing_migrations(self):
        output = StringIO()
        options = {
            'interactive': False,
            'dry_run': True,
            'stdout': output,
            'check_changes': True,
            'verbosity': 3
        }

        try:
            call_command('makemigrations', 'djangocms_youtube_lazyload', **options)
        except SystemExit as e:
            status_code = str(e)
        else:
            # the "no changes" exit code is 0
            status_code = '0'

        if status_code == '1':
            self.fail('There are missing migrations:\n {}'.format(output.getvalue()))