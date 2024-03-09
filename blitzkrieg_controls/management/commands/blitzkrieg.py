from django.conf import settings
# from django.db import models
from django.contrib.contenttypes import models as contrib_models
from django.apps.config import import_string
from django.apps.config import os
from django.core.management import call_command
from django.core.management import BaseCommand

from blitzkrieg_controls.management.utils import validate_options


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-A', '--all_apps_true', action='store_true', help='To run for all USER_APPS in settings.py'
        )
        parser.add_argument(
            '--app_label', type=str, dest='app_label', help='To run for the specified app in'
                                                            ' USER_APPS in settings.py'
        )
        parser.add_argument(
            '--model_name', type=str, dest='model_name', help='To run for the specified model in '
                                                              'USER_APPS in settings.py '
                                                              'format :: app_label.model_name'
        )

    def handle(self, *args, **options):
        validate_options(options)
        if options.get('all_apps_true', False):
            # content_types = _get_content_types(None)
            # content_types_dict = get_content_types_dict(content_types)
            # import ipdb; ipdb.set_trace()

            for app in settings.USER_APPS:
                call_command(
                    f'blitzkrieg_serializers',
                    app_label=app
                    # model_name=content_type.model_class().__name__,
                )
                call_command(
                    f'blitzkrieg_views',
                    # model_name=content_type.model_class().__name__,
                    app_label=app
                )
                call_command(
                    f'blitzkrieg_admins',
                    # model_name=content_type.model_class().__name__,
                    app_label=app
                )
