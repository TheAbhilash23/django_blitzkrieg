from django.contrib import admin
from basic_app import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

        list_display = (
            'id',
            'title',
            'pages',
            'cover_page',
            'user',
            
        )



