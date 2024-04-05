from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, RedirectView, DetailView, UpdateView, DeleteView
from CycleShop.accounts.forms import CycleShopUserCreationForm, ProfileForm
from CycleShop.accounts.models import Profile

UserModel = get_user_model()


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


class ProfileDeleteView(DeleteView):
    model = UserModel
    template_name = "accounts/profile_delete.html"
    success_url = reverse_lazy("home_page")

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())




