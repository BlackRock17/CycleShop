from django import forms

from CycleShop.components.models import ComponentsType


class ComponentFilterForm(forms.Form):
    category = forms.ChoiceField(
        choices=ComponentsType.choices,
        widget=forms.RadioSelect,
        required=True,
    )
