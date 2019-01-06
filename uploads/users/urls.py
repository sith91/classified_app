from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from rest_framework import routers
from uploads.users import views




router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
# post views
url(r'^login/$',  auth_views.login, {'template_name': 'login.html'}, name='login'),
url(r'^logout/$', auth_views.logout,{'next_page': '/'},name='logout'),
url(r'^edit_profile/$',views.update_profile, name='edit_profile'),
url(r'^', include(router.urls))
]