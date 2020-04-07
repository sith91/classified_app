from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import routers
from uploads.users import views
from uploads.users.forms import Login

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

app_name = 'users'

urlpatterns = [
# post views
url(r'^login/$',  LoginView.as_view(template_name='login.html'),{'authentication_form': Login}, name='login'),
url(r'^logout/$', LogoutView.as_view(next_page='/'), name='logout'),
#url(r'^edit_profile/$',views.update_profile, name='edit_profile'),
url(r'^signup/$', views.signup, name='signup'),
url(r'^profile/(?P<username>\w+)$', views.profile, name='profile'),
url(r'^', include(router.urls))
]