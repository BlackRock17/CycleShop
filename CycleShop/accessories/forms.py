from django import forms
from .models import Category


class AccessoryCategoryForm(forms.Form):
    category = forms.ChoiceField(
        choices=Category.choices,
        widget=forms.RadioSelect,
        required=True
    )
