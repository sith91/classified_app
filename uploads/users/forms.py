from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User

from uploads.users.models import Profile
from django.core.files.images import get_image_dimensions

class Login(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','password')


class SignUpForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    business_reg = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    avatar = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','email','business_reg','avatar', 'password1', 'password2', )

"""

class Userform(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    #email = forms.EmailField(widget=forms.EmailField(attrs={'class':'form-control'}))

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):

    business_reg = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    #avatar = forms.FileField(widget=forms.FileField(attrs={'class':'form-control'}))

    class Meta():
        model = Profile
        fields = ('business_reg','avatar')

"""