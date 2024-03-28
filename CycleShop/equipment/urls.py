from django.urls import path

from CycleShop.equipment.views import EquipmentsListView, EquipmentCategoryListView

urlpatterns = (
    path("", EquipmentsListView.as_view(), name="equipments_list"),
    path('category/<str:category>/', EquipmentCategoryListView.as_view(), name='equipment_category_list'),
)