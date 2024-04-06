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


class CheckoutForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    town = forms.CharField(max_length=100, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    postcode = forms.CharField(max_length=20, required=True)

    class Meta:
        model = Profile
        fields = ['full_name', 'email', 'town', 'address', 'postcode']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['full_name'].initial = self.user.profile.get_full_name()
            self.fields['email'].initial = self.user.profile.email
            self.fields['town'].initial = self.user.profile.town
            self.fields['address'].initial = self.user.profile.address
            self.fields['postcode'].initial = self.user.profile.postcode