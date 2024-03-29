from django import forms
from .models import MountainBicycleCategory, RoadBicycleCategory, ElectricBicycleCategory, TyreSize, BicycleSize


class BicycleFilterForm(forms.Form):
    BICYCLE_CATEGORIES = (
        ('MountainBicycle', 'Mountain Bicycle'),
        ('RoadBicycle', 'Road Bicycle'),
        ('ElectricBicycle', 'Electric Bicycle'),
    )

    category = forms.ChoiceField(choices=BICYCLE_CATEGORIES, required=False, label='Category', widget=forms.RadioSelect)


class BicycleCategoryFilterForm(forms.Form):

    def __init__(self, category=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if category == 'MountainBicycle':
            self.fields['category'] = forms.ChoiceField(choices=MountainBicycleCategory.choices, required=False, widget=forms.RadioSelect)
        elif category == 'RoadBicycle':
            self.fields['category'] = forms.ChoiceField(choices=RoadBicycleCategory.choices, required=False, widget=forms.RadioSelect)
        elif category == 'ElectricBicycle':
            self.fields['category'] = forms.ChoiceField(choices=ElectricBicycleCategory.choices, required=False, widget=forms.RadioSelect)

        self.fields['tyres_size'] = forms.ChoiceField(choices=TyreSize.choices, required=False, label='Tyre_Size', widget=forms.RadioSelect)
        self.fields['size'] = forms.ChoiceField(choices=BicycleSize.choices, required=False, label='Size', widget=forms.RadioSelect)
