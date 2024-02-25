import os
from django.core.management import BaseCommand
from blitzkrieg_controls.definitions import ModelDetails
from blitzkrieg_controls.management.utils import validate_options, validate_serializers_options, get_content_types_dict
from blitzkrieg_controls.settings import BLITZKRIEG
from blitzkrieg_controls.views import create_serializers_dot_py


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
        base_serializers_module, base_serializers_serializer = BLITZKRIEG['base_model_serializer'].split('.')[0:-1], BLITZKRIEG['base_model_serializer'].split('.')[-1]
        base_serializers_module = '.'.join(base_serializers_module)
        content_type_dict = get_content_types_dict(app_label)
        modelset: list = content_type_dict[app_label]
        # import ipdb; ipdb.set_trace()

        context = {
            'app_name': app_label,
            'base_model_serializer_module': base_serializers_module,
            'base_model_serializer_serializer': base_serializers_serializer,
            'modelset': modelset
        }
        template_address = os.path.join(os.getcwd() + '/templates/blitzkrieg/serializers.html')
        create_serializers_dot_py(template_address, context)



