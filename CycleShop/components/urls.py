from django.urls import path

from CycleShop.components.views import ComponentsListView, ComponentDetailView

urlpatterns = (
    path("<int:pk>/", ComponentDetailView.as_view(), name="component_detail"),
    path("", ComponentsListView.as_view(), name="components_list"),
)
