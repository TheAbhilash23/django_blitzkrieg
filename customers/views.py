from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from customers import models
from customers import serializers


class CustomerView(ModelSerializer):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class CustomerCreditRiskParameterView(ModelSerializer):
    queryset = models.CustomerCreditRiskParameter.objects.all()
    serializer_class = serializers.CustomerCreditRiskParameterSerializer


