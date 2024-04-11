from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import handler404

from CycleShop import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("CycleShop.common.urls")),
    path("bicycles/", include("CycleShop.bicycles.urls")),
    path("equipments/", include("CycleShop.equipment.urls")),
    path("components/", include("CycleShop.components.urls")),
    path("accessories/", include("CycleShop.accessories.urls")),
    path("accounts/", include("CycleShop.accounts.urls")),
    path("images/", include("CycleShop.images.urls")),
    path("cart/", include("CycleShop.cart.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('404/', TemplateView.as_view(template_name='404.html'), name='404'),
    ]


handler404 = 'CycleShop.common.views.handler404'