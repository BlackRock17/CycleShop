from django import forms
from .models import GogglesCategory, ProtectionCategory, HelmetCategory, GlovesCategory


class EquipmentFilterForm(forms.Form):
    search_query = forms.CharField(
        label='Search',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search equipments...'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['goggles_categories'] = forms.BooleanField(required=False, widget=forms.RadioSelect(
            choices=[(category.name, category.value) for category in GogglesCategory]
        ))
        self.fields['protection_categories'] = forms.BooleanField(required=False, widget=forms.RadioSelect(
            choices=[(category.name, category.value) for category in ProtectionCategory]
        ))
        self.fields['helmet_categories'] = forms.BooleanField(required=False, widget=forms.RadioSelect(
            choices=[(category.name, category.value) for category in HelmetCategory]
        ))
        self.fields['gloves_categories'] = forms.BooleanField(required=False, widget=forms.RadioSelect(
            choices=[(category.name, category.value) for category in GlovesCategory]
        ))