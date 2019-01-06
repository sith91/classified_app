from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profiles

class ProfileInline(admin.StackedInline):
    model = Profiles
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'vendor'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    def phone_number(self,instance):
        return instance.profiles.phone_number
        phone_number.short_description = 'phone_number'

    def business_reg(self,instance):
        return instance.profiles.business_reg
        business_reg.short_description = 'business_reg'



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)