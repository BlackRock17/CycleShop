from django.urls import path

from CycleShop.accounts.views import LogInUserView, RegisterUserView, LogOutView

urlpatterns = (
    path("login/", LogInUserView.as_view(), name="login"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("logout/", LogOutView.as_view(), name="logout"),
)