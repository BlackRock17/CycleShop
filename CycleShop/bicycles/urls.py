from django.urls import path

from CycleShop.bicycles.views import BicycleListView, BicycleDetailView

urlpatterns = (
    path('bicycles/<str:category>/', BicycleListView.as_view(), name='bicycle_list'),
    path('bicycle/<int:pk>/', BicycleDetailView.as_view(), name='bicycle_detail'),
)
