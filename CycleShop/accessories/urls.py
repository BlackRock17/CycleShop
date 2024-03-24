from django.urls import path

from CycleShop.accessories.views import AccessoriesListView, AccessoryDetailView

urlpatterns = (
    path('<int:pk>/', AccessoryDetailView.as_view(), name='accessory_detail'),
    path('', AccessoriesListView.as_view(), name='accessories_list'),
    path('<str:category>/', AccessoriesListView.as_view(), name='accessories_list_by_category'),

)
