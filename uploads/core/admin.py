from django.contrib import admin
# Register your models here.
from uploads.core.models import Deals,Category


class DModelAdmin(admin.ModelAdmin):
    list_display = ["description"]


admin.site.register(Deals,DModelAdmin)


class CModelAdmin(admin.ModelAdmin):
    list_display = ["mname","mdescription"]


admin.site.register(Category, CModelAdmin)

