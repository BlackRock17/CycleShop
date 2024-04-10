from django.urls import path

from CycleShop.equipment.views import EquipmentsListView, EquipmentCategoryListView, EquipmentDetailView

urlpatterns = (
    path("<int:pk>/", EquipmentDetailView.as_view(), name="equipment_detail"),
    path("", EquipmentsListView.as_view(), name="equipments_list"),
    path("<str:category>/", EquipmentCategoryListView.as_view(), name="equipment_category_list"),
)
