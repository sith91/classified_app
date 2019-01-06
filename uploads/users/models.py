from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profiles(models.Model):
    vendor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='"profile"+')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    business_reg = models.TextField(max_length=10,unique=True)
    website = models.URLField()


    def __str__(self):  # __unicode__ for Python 2
        return self.vendor.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profiles.objects.create(vendor=instance)

   # @receiver(post_save, sender=User)
   # def save_user_profile(sender, instance, **kwargs):
      #  instance.u