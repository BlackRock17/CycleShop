from django.apps import apps
from django.shortcuts import render
from django.views import generic as views

from CycleShop.accessories.models import Category
from CycleShop.bicycles.models import MountainBicycleCategory, RoadBicycleCategory, ElectricBicycleCategory
from CycleShop.components.models import ComponentsType
from CycleShop.equipment.models import Equipment


class HomePageView(views.TemplateView):
    template_name = "common/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['mountain_bike_categories'] = MountainBicycleCategory.choices
        context['road_bike_categories'] = RoadBicycleCategory.choices
        context['electric_bike_categories'] = ElectricBicycleCategory.choices

        models_module = apps.get_app_config('equipment').get_models()
        equipment_classes = [cls for cls in models_module if isinstance(cls, type) and issubclass(cls, Equipment) and cls != Equipment]

        equipment_class_names = {cls: cls.__name__ for cls in equipment_classes}

        context['equipment_class_names'] = equipment_class_names

        context['components_types'] = ComponentsType.choices

        context["accessories_types"] = Category.choices

        return context
