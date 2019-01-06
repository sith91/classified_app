from AptUrl.Helpers import _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.checks import messages
from django.db import transaction
from django.shortcuts import redirect, render
from rest_framework import viewsets
from uploads.users.serializers import UserSerializer, GroupSerializer


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        from uploads.users.forms import UserForm
        user_form = UserForm(request.POST, instance=request.user)
        from uploads.users.forms import ProfileForm
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.vendor)
    return render(request, 'profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



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