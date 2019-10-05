from django.contrib import admin

from .models import CustomUser, Settings


class SettingsInline(admin.StackedInline):
    model = Settings


class CustomUserAdmin(admin.ModelAdmin):
    inlines = [SettingsInline, ]

admin.site.register(CustomUser, CustomUserAdmin)