from django.contrib import admin
from mfa_themes.models import MfaTheme


class MfaThemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'theme_zip', 'active')
    search_field = ('title', 'theme_zip')

admin.site.register(MfaTheme, MfaThemeAdmin)
