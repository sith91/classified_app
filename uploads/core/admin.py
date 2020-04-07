from django.contrib import admin
# Register your models here.
from uploads.core.models import Deals,Category, SubCategory


class DModelAdmin(admin.ModelAdmin):
    list_display = ["description"]


admin.site.register(Deals,DModelAdmin)


class CModelAdmin(admin.ModelAdmin):
    list_display = ["mname","mdescription"]


admin.site.register(Category, CModelAdmin)

class SCModelAdmin(admin.ModelAdmin):
    list_display = ["category","scname","scdecription"]

admin.site.register(SubCategory, SCModelAdmin)

