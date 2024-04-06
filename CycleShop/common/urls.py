from django.urls import path

from CycleShop.common.views import HomePageView, order_history

urlpatterns = (
    path("", HomePageView.as_view(), name="home_page"),
    path("history/", order_history, name="order_history"),
)
