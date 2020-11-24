from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext, gettext_lazy as _

from .models import User, Role

# Register your models here.
class UserAdmin(DjangoUserAdmin):
    list_display = ['email', 'first_name', 'last_name']
    list_filter = tuple()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': (('first_name', 'last_name'), 'birth_date')}),
        (_('Permissions'), {
            'fields': ('role',),
        }),
        (_('Important dates'), {
            'fields': (('date_joined','last_login'),),
        })
    )

    base_add_fields = (
        (None, {'fields': ('email', 'password1', 'password2'),}),
        (_('Personal info'), {'fields': (('first_name', 'last_name'), 'birth_date')}),
        (_('Permissions'), {
            'fields': ('role',),
        }),
    )

    add_fieldsets = base_add_fields

    readonly_fields = ('date_joined', 'last_login')

admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.unregister(Group)
