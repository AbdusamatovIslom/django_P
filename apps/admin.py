from django.contrib import admin

from apps.models import Project


@admin.register(Project)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['first_name']