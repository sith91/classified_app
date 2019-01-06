from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url(r'^',include("uploads.core.urls",namespace='deals')),
    url(r'^',include("uploads.users.urls",namespace='users')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include("rest_framework.urls", namespace='rest_framework'))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
