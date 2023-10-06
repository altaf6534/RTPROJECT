from django.db import models
from django.contrib import admin
from API.UserManagementAPI.models import UserType,OTP
from API.UserManagementAPI import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
# Create your models here.

class UserAdmin(BaseUserAdmin):
    ordering = ['pkid']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal Info'), {'fields': ('name', 'country_code', 'mobile', 'user_type')}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile', 'password1', 'password2',)
        }),
    )


admin.site.register(models.User, UserAdmin)





@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
     list_display = [f.name for f in OTP._meta.fields]

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
     list_display = [f.name for f in UserType._meta.fields]
