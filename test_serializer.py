from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from customers import models


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = models.Customer
        fields = (
            'customer_credit_risk_parameters',
            'id',
            'name',
            'telephone',
            'email',
            'social_media_link',
            'highest_education',
            
        )


class CustomerCreditRiskParameterSerializer(ModelSerializer):

    class Meta:
        model = models.CustomerCreditRiskParameter
        fields = (
            'id',
            'customer',
            'is_good_credit_risk',
            'status',
            'duration',
            'credit_history',
            'purpose',
            'amount',
            'savings',
            'employment_duration',
            'installment_rate',
            'personal_status_sex',
            'other_debtors',
            'present_residence',
            'most_valuable_property',
            'age',
            'other_installment_plans',
            'housing',
            'number_credits',
            'job',
            'people_liable',
            'has_telephone',
            'is_foreign_worker',
            
        )


