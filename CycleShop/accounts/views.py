from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView
from CycleShop.accounts.forms import CycleShopUserCreationForm


class LogInUserView(LoginView):
    template_name = "accounts/login_user.html"
    redirect_authenticated_user = True


class RegisterUserView(CreateView):
    template_name = "accounts/register_user.html"
    form_class = CycleShopUserCreationForm
    success_url = reverse_lazy("home_page")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result


class LogOutView(RedirectView):
    url = reverse_lazy("home_page")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
