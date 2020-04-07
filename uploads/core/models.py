from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    mname = models.CharField(max_length=100, blank=False,unique=True)
    mdescription = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.mname

    class Meta:
        ordering = ('mname',)

class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    scname = models.CharField (max_length=100, blank=False,unique=True)
    scdecription = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.scname

    class Meta:
        ordering = ('scname',)

class Deals(models.Model):

    vendor_deal = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null= True)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateField(auto_now_add=True)
    expire_date = models.DateField(null=False)
    current_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.description


    class Meta:

        ordering = ('description',)




