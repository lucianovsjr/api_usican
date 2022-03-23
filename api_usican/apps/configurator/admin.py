from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import CustomOption, CustomOptionItem


admin.site.register(Permission)

admin.site.register(CustomOption)
admin.site.register(CustomOptionItem)
