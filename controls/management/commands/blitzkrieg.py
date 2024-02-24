from django.conf import settings
# from django.db import models
from django.contrib.contenttypes import models as contrib_models
from django.apps.config import import_string
from django.apps.config import os
from django.core.management import call_command
from django.core.management import BaseCommand


def _get_content_types():
    user_apps_models = contrib_models.ContentType.objects.filter(
        app_label__in=settings.USER_APPS
    )
    return user_apps_models


class Command(BaseCommand):
    def handle(self, *args, **options):
        content_types = _get_content_types()
        for content_type in content_types:
            model_fields = content_type.model_class()._meta.get_fields()
            fields = []
            for field in model_fields:
                if field.get_internal_type() not in ('ForeignKey', 'OneToOneField', 'ManyToManyField'):
                    fields.append((field.name, field.get_internal_type()))
            call_command(
                f'create_serializers',
                fields.__str__(),
                model_name=content_type.model_class().__name__,
                app_label=content_type.app_label
            )
