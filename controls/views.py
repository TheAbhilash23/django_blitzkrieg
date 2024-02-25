import os

# Create your views here.
from django.template.loader import get_template


def create_serializers_dot_py(template_address: str, context: dict):
    print(template_address)
    template = get_template(template_address)

    rendered_template = None
    output_file_path = 'tests/test_serializer.py'

    try:
        rendered_template = template.render(context)
        with open(output_file_path, 'w') as f:
            f.write(rendered_template)
    except Exception as e:
        print('error was', e)
    print(f"Rendered template saved to: {output_file_path}")
