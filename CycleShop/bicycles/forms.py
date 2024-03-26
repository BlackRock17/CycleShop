from django import forms
from .models import MountainBicycleCategory, RoadBicycleCategory, ElectricBicycleCategory, TyreSize, BicycleSize


class BicycleFilterForm(forms.Form):
    def __init__(self, category=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if category == 'mountain':
            self.fields['category'] = forms.ChoiceField(choices=MountainBicycleCategory.choices, required=False, widget=forms.RadioSelect)
        elif category == 'road':
            self.fields['category'] = forms.ChoiceField(choices=RoadBicycleCategory.choices, required=False, widget=forms.RadioSelect)
        elif category == 'electric':
            self.fields['category'] = forms.ChoiceField(choices=ElectricBicycleCategory.choices, required=False, widget=forms.RadioSelect)

        self.fields['tyres_size'] = forms.ChoiceField(choices=TyreSize.choices, required=False)
        self.fields['size'] = forms.ChoiceField(choices=BicycleSize.choices, required=False)
