from django import forms

from CycleShop.equipment.models import EquipmentSize, Equipment


class EquipmentFilterForm(forms.Form):
    EQUIPMENT_CHOICES = [
        ("Goggles", "Goggles"),
        ("Protection", "Protection"),
        ("Helmet", "Helmet"),
        ("Gloves", "Gloves"),
    ]

    category = forms.ChoiceField(choices=EQUIPMENT_CHOICES, required=False, label="Category", widget=forms.RadioSelect)


class TypeEquipmentFilterForm(forms.Form):
    category = forms.ChoiceField(choices=[], required=False, label="Category", widget=forms.RadioSelect)
    size = forms.ChoiceField(choices=EquipmentSize.choices, required=False, label="Size", widget=forms.RadioSelect)

    def __init__(self, equipment_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].choices = Equipment.get_category_choices(equipment_type)