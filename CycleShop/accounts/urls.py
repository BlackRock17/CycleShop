from django.urls import path, include

from CycleShop.accounts.views import LogInUserView, RegisterUserView, LogOutView, ProfileDetailsView, ProfileEditView, \
    ProfileDeleteView

urlpatterns = (
    path("login/", LogInUserView.as_view(), name="login"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("profile/<int:pk>/", include([
        path("", ProfileDetailsView.as_view(), name="profile_details"),
        path("edit/", ProfileEditView.as_view(), name="profile_edit"),
        path("delete/", ProfileDeleteView.as_view(), name="profile_delete")
    ]))
)