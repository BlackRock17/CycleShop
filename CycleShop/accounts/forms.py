from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from CycleShop.accounts.models import Profile

UserModel = get_user_model()


class CycleShopUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'town', 'address', 'postcode']