from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib import admin

from apps.users.models import User, Driver, Rider, Services


class UserAdmin(DefaultUserAdmin):
    list_display = ('mobile_phone', 'role')


admin.site.register(User, UserAdmin)
admin.site.register(Rider)
admin.site.register(Driver)
admin.site.register(Services)