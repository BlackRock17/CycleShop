from django.urls import path

from CycleShop.accessories.views import AccessoriesListView

urlpatterns = (
    path('accessories/', AccessoriesListView.as_view(), name='accessories_list'),
    path('accessories/<str:category>/', AccessoriesListView.as_view(), name='accessories_list_by_category'),
)
