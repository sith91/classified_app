from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from uploads.users.models import Profiles


class Login(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ('vendor', 'phone_number', 'website')


