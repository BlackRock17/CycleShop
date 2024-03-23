from django.urls import path

from CycleShop.accessories.views import AccessoriesListView, AccessoryDetailView

urlpatterns = (
    path('accessories/<int:pk>/', AccessoryDetailView.as_view(), name='accessory_detail'),
    path('accessories/', AccessoriesListView.as_view(), name='accessories_list'),
    path('accessories/<str:category>/', AccessoriesListView.as_view(), name='accessories_list_by_category'),

)
