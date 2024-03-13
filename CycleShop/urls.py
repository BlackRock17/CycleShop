from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from CycleShop import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("bicycles/", include("CycleShop.bicycles.urls"),)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
