from django.urls import path

from CycleShop.equipment.views import EquipmentsListView

urlpatterns = (
    path("", EquipmentsListView.as_view(), name="equipments_list"),
)