from django.contrib import admin
from basic_app import models


@admin.register(models.Book)
class BookAdmin((admin.ModelAdmin):

        list_disply = (
            'id',
            'title',
            'pages',
            'cover_page',
            'user',
            
        )



