from django.contrib import admin

from apps.models import CustomUser


# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age']