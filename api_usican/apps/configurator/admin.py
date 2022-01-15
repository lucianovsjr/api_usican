from django.contrib import admin

from .models import CustomOption, CustomOptionItem

admin.site.register(CustomOption)
admin.site.register(CustomOptionItem)
