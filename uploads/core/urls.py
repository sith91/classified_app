from django.conf.urls import url, include
from rest_framework import routers
from .views import home,model_form_upload, DealViewSet

app_name = "core"

router = routers.DefaultRouter()
router.register(r'deals_list', DealViewSet)

urlpatterns = [

    url(r'^$',home, name='home'),
   # url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    url(r'^form/$', model_form_upload, name='model_form_upload'),
    url(r'^', include(router.urls)),
]