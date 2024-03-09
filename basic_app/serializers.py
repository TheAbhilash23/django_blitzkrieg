from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from basic_app import models


class BookSerializer(ModelSerializer):

    class Meta:
        model = models.Book
        fields = (
            'id',
            'title',
            'pages',
            'cover_page',
            'user',
            
        )


