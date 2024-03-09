from django.contrib import admin
from customers import models


@admin.register(models.Customer)
class CustomerAdmin((admin.ModelAdmin):

        list_disply = (
            'customer_credit_risk_parameters',
            'id',
            'name',
            'telephone',
            'email',
            'social_media_link',
            'highest_education',
            
        )



@admin.register(models.CustomerCreditRiskParameter)
class CustomerCreditRiskParameterAdmin((admin.ModelAdmin):

        list_disply = (
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



