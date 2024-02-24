from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Book(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=225
    )
    pages = models.IntegerField(
        _('Pages'),
        validators=[MinValueValidator(0)]
    )
    cover_page = models.FileField()
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='book'
    )

