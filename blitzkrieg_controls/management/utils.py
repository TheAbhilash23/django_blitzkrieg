from django.conf import settings
# from django.db import models
from django.contrib.contenttypes import models as contrib_models
from django.core.management import CommandError
from django.db.models import QuerySet

from blitzkrieg_controls.definitions import ModelDetails


def _get_content_types(app_label: str | None) -> QuerySet:
    if not app_label:
        user_apps_models = contrib_models.ContentType.objects.filter(
            app_label__in=settings.USER_APPS
        )
    else:
        user_apps_models = contrib_models.ContentType.objects.filter(
            app_label=app_label
        )
    return user_apps_models


def get_content_types_dict(app_label: str | None) -> dict:
    content_queryset = _get_content_types(app_label)
    return_dict = {app.app_label: [] for app in content_queryset}
    for content_type in content_queryset:
        # import ipdb; ipdb.set_trace()
        model_fields = content_type.model_class()._meta.get_fields()
        fields = []
        for field in model_fields:
            fields.append(field.name)
        model_details = ModelDetails(
            app_name=content_type.app_label,
            pascal_model_name=content_type.model_class().__name__,
            fields=fields,
        )
        return_dict[content_type.app_label].append(model_details)

    return return_dict


def validate_options(options: dict) -> None:
    allowed_options = ('all_apps_true', 'app_label', 'model_name')
    print(options)
    counter = 0
    for option in allowed_options:
        if options.get(option):
            print(options[option])
            counter += 1

    if counter != 1:
        raise CommandError('You need to use only one option to run this command '
                           'choose from: --%s' % ', --'.join(allowed_options))
    return None


def validate_serializers_options(options: dict) -> None:
    allowed_options = ('app_label', 'model_name')
    print(options)
    counter = 0
    for option in allowed_options:
        if options.get(option):
            print(options[option])
            counter += 1

    if counter != 1:
        raise CommandError('You need to use only one option to run this command '
                           'choose from: --%s' % ', --'.join(allowed_options))
    return None


def validate_admin_options(options: dict) -> None:
    allowed_options = ('app_label', 'model_name')
    print(options)
    counter = 0
    for option in allowed_options:
        if options.get(option):
            print(options[option])
            counter += 1

    if counter != 1:
        raise CommandError('You need to use only one option to run this command '
                           'choose from: --%s' % ', --'.join(allowed_options))
    return None


def validate_views_options(options: dict) -> None:
    allowed_options = ('app_label', 'model_name')
    print(options)
    counter = 0
    for option in allowed_options:
        if options.get(option):
            print(options[option])
            counter += 1

    if counter != 1:
        raise CommandError('You need to use only one option to run this command '
                           'choose from: --%s' % ', --'.join(allowed_options))
    return None
