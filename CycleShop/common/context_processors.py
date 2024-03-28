from django.apps import apps
from CycleShop.accessories.models import Category
from CycleShop.bicycles.models import MountainBicycleCategory, RoadBicycleCategory, ElectricBicycleCategory
from CycleShop.components.models import ComponentsType
from CycleShop.equipment.models import Equipment


def categories(request):
    return {
        "bicycle_categories": {
            "mountain": "mountain_bicycle_list",
            "road": "road_bicycle_list",
            "electric": "electric_bicycle_list",
        },
        "equipment_class_names": get_equipment_class_names(),
        "components_types": ComponentsType.choices,
        "accessories_categories": Category.choices,
    }


def get_equipment_class_names():
    models_module = apps.get_app_config("equipment").get_models()
    equipment_classes = [cls for cls in models_module if isinstance(cls, type) and issubclass(cls, Equipment) and cls != Equipment]
    return {cls.__name__: cls.__name__ for cls in equipment_classes}
