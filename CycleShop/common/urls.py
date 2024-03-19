from django.urls import path

from CycleShop.common.views import HomePageView

urlpatterns = (
    path("", HomePageView.as_view(), name="home_page"),
)
