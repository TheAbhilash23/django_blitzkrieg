from django.core.management import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'fields_str', type=str,
        )
        parser.add_argument(
            '--app_label', type=str, dest='app_label',
        )
        parser.add_argument(
            '--model_name', type=str, dest='model_name',
        )

    def handle(self, *args, **options):
        # import ipdb;ipdb.set_trace()
        print(options['fields_str'])
        print(options['app_label'])
        print(options['model_name'])


