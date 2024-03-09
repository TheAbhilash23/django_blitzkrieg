from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from basic_app import models
from basic_app import serializers


class BookView(ModelSerializer):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


