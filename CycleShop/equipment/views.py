from django.apps import apps
from django.db.models import Field
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic as views

from CycleShop.equipment.forms import EquipmentFilterForm, TypeEquipmentFilterForm
from CycleShop.equipment.models import Equipment, Goggles, Protection, Helmet, Gloves


class EquipmentsListView(views.ListView):
    template_name = "equipments/equipments_list.html"
    paginate_by = 6
    context_object_name = "equipment_list"

    def get_queryset(self):
        queryset = Equipment.objects.all()
        form = EquipmentFilterForm(self.request.GET)
        if form.is_valid():
            category = form.cleaned_data["category"]
            if category:
                self.request.GET = self.request.GET.copy()
                self.request.GET["category"] = category
                return queryset
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = EquipmentFilterForm(self.request.GET)
        return context

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        form = EquipmentFilterForm(request.GET)
        if form.is_valid():
            category = form.cleaned_data["category"]
            if category:
                return redirect(reverse("equipment_category_list", kwargs={"category": category}))
        return super().get(request, *args, **kwargs)


class EquipmentCategoryListView(views.ListView):
    template_name = "equipments/equipment_category_list.html"
    paginate_by = 20
    context_object_name = "equipment_list"

    def get_queryset(self):
        category = self.kwargs["category"]
        model = apps.get_model("equipment", category)

        if model:
            queryset = model.objects.all()
            form = TypeEquipmentFilterForm(category, self.request.GET)

            if form.is_valid():
                category_filter = form.cleaned_data.get("category")
                size_filter = form.cleaned_data.get("size")

                if category_filter:
                    queryset = queryset.filter(category=category_filter)
                if size_filter:
                    queryset = queryset.filter(size=size_filter)
        else:
            queryset = Equipment.objects.none()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs["category"]
        context["category"] = category
        context["form"] = TypeEquipmentFilterForm(category, self.request.GET)
        return context


class EquipmentDetailView(views.DetailView):
    model = Equipment
    template_name = "equipments/equipment_detail.html"
    context_object_name = "equipment"
    queryset = Equipment.objects.select_related("goggles", "protection", "helmet", "gloves")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        equipment = self.get_object()
        equipment_fields = []

        # for field in equipment._meta.fields:
        #     if field.name not in ("id", "quantity"):
        #         verbose_name = field.verbose_name
        #         value = getattr(equipment, field.name)
        #         equipment_fields.append({"verbose_name": verbose_name, "value": value})

        specific_models = {
            "goggles": Goggles,
            "protection": Protection,
            "helmet": Helmet,
            "gloves": Gloves
        }

        for model_name, model_class in specific_models.items():
            if hasattr(equipment, model_name):
                specific_model = getattr(equipment, model_name)
                for field in model_class._meta.get_fields():
                    if field.name not in ["id", "equipment_ptr", "quantity", "price"] and isinstance(field, Field):
                        verbose_name = field.verbose_name
                        value = getattr(specific_model, field.name)
                        equipment_fields.append({"verbose_name": verbose_name, "value": value})
                break

        context["equipment_fields"] = equipment_fields

        return context
