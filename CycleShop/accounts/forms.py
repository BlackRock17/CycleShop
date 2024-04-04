from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


class CycleShopUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserModel
