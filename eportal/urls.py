
from django.contrib import admin
from django.urls import path, include

from django.conf import settings #add this
from django.conf.urls.static import static #add this


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
