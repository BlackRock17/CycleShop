from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, RedirectView, DetailView, UpdateView, DeleteView
from CycleShop.accounts.forms import CycleShopUserCreationForm, ProfileForm
from CycleShop.accounts.models import Profile


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


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = "accounts/profile_details.html"


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "accounts/profile_edit.html"

    def get_success_url(self):
        return reverse("profile_details", kwargs={
            "pk": self.object.pk,
        })


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = "accounts/delete_profile.html"
    success_url = reverse_lazy("home_page")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())




