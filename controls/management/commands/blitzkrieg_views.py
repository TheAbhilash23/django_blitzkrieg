import os
from django.core.management import BaseCommand
from controls.definitions import ModelDetails
from controls.management.utils import validate_options, validate_serializers_options, get_content_types_dict
from controls.settings import BLITZKRIEG
from controls.views import create_views_dot_py


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--app_label', type=str, dest='app_label', help='To run for the specified app in'
                                                            ' USER_APPS in settings.py'
        )
        parser.add_argument(
            '--model_name', type=str, dest='model_name', help='To run for the specified model in '
                                                              'USER_APPS in settings.py '
                                                              'format :: app_label.model_name '
                                                              'Use same model name as in models.py'
        )

    def handle(self, *args, **options):
        validate_serializers_options(options)
        print('app is:: ', options['app_label'])
        app_label = options['app_label']
        if options.get('model_name'):
            app_label, model_name = options['model_name'].split('.')
            print('model_name is:: ', model_name)
        base_viewset_module, base_viewset_class = BLITZKRIEG['base_model_serializer'].split('.')[0:-1], BLITZKRIEG['base_model_serializer'].split('.')[-1]
        base_viewset_module = '.'.join(base_viewset_module)
        content_type_dict = get_content_types_dict(app_label)
        modelset: list = content_type_dict[app_label]
        # import ipdb; ipdb.set_trace()

        context = {
            'app_name': app_label,
            'base_generic_model_viewset_module': base_viewset_module,
            'base_generic_model_viewset_viewset': base_viewset_class,
            'modelset': modelset
        }
        template_address = os.path.join(os.getcwd() + '/templates/blitzkrieg/views.html')
        create_views_dot_py(template_address, context)



