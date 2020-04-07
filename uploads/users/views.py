from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
from uploads.users.forms import SignUpForm # Userform, UserProfileInfoForm
from uploads.users.serializers import UserSerializer, GroupSerializer
from uploads.core.models import Deals

"""
def user_login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('http://127.0.0.1:8000')
                else:
                    return HttpResponse("Your account was inactive.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})

"""


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.business_reg = form.cleaned_data.get('business_reg')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


@csrf_protect
def profile(request,username):

    user = User.objects.get(username = username )
    #profile = Profile.objects.get(user=user)
    user_posts = Deals.objects.filter(vendor_deal__exact = user)
    return render(request,'profile.html',{'user':user,'user_posts':user_posts})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    """
    register = template.Library()

    @register.filter
    def check_login(request):
        if request.user.is_authenticated():
            return True
        else:
            return False"""