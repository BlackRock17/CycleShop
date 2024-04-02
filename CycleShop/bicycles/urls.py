from django.urls import path

from CycleShop.bicycles.views import BicycleCategoryListView, BicycleDetailView, BicycleListView

urlpatterns = (
    path("<int:pk>/", BicycleDetailView.as_view(), name="bicycle_detail"),
    path("<str:category>/", BicycleCategoryListView.as_view(), name="bicycle_category_list"),
    path("", BicycleListView.as_view(), name="bicycle_list")
)
