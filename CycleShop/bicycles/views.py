from django.db.models import Field
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic as views
from CycleShop.bicycles.forms import BicycleFilterForm, BicycleCategoryFilterForm
from CycleShop.bicycles.models import MountainBicycle, RoadBicycle, ElectricBicycle, Bicycle


class BicycleListView(views.ListView):
    template_name = "bicycle/bicycle_list.html"
    paginate_by = 20
    context_object_name = "bicycles"

    def get_queryset(self):
        queryset = Bicycle.objects.all()
        form = BicycleFilterForm(self.request.GET)
        if form.is_valid():
            category = form.cleaned_data["category"]
            if category:
                self.request.GET = self.request.GET.copy()
                self.request.GET["category"] = category
                return queryset
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BicycleFilterForm(self.request.GET)
        return context

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        form = BicycleFilterForm(request.GET)
        if form.is_valid():
            category = form.cleaned_data["category"]
            if category:
                return redirect(reverse("bicycle_category_list", kwargs={"category": category}))
        return super().get(request, *args, **kwargs)


class BicycleCategoryListView(views.ListView):
    template_name = "bicycle/bicycle_category_list.html"
    context_object_name = "bicycles"
    paginate_by = 20

    def get_queryset(self):
        category = self.kwargs["category"]
        queryset = self.get_bicycle_queryset(category)

        form = BicycleCategoryFilterForm(category, self.request.GET)
        if form.is_valid():
            filters = {
                key: value for key, value in form.cleaned_data.items() if value
            }
            queryset = queryset.filter(**filters)

        return queryset

    @staticmethod
    def get_bicycle_queryset(category):
        if category == "MountainBicycle":
            return MountainBicycle.objects.all()
        elif category == "RoadBicycle":
            return RoadBicycle.objects.all()
        elif category == "ElectricBicycle":
            return ElectricBicycle.objects.all()
        else:
            return MountainBicycle.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs["category"]
        context["category"] = category
        context["form"] = BicycleCategoryFilterForm(category, self.request.GET)

        context["category_names"] = {
            "MountainBicycle": "Mountain Bicycle",
            "RoadBicycle": "Road Bicycle",
            "ElectricBicycle": "Electric Bicycle",
        }

        return context


class BicycleDetailView(views.DetailView):
    model = Bicycle
    template_name = "bicycle/bicycle_detail.html"
    context_object_name = "bicycle"
    queryset = Bicycle.objects.select_related("mountainbicycle", "roadbicycle", "electricbicycle")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bicycle = self.get_object()

        context["images"] = bicycle.bicycle_images.all()

        context["bicycle_fields"] = []

        specific_models = {
            "mountainbicycle": MountainBicycle,
            "electricbicycle": ElectricBicycle,
            "roadbicycle": RoadBicycle,
        }

        for model_name, model_class in specific_models.items():
            if hasattr(bicycle, model_name):
                specific_model = getattr(bicycle, model_name)
                for field in model_class._meta.get_fields():
                    if field.name not in ["id", "bicycle_ptr", "quantity"] and isinstance(field, Field):
                        verbose_name = field.verbose_name
                        value = getattr(specific_model, field.name)
                        context["bicycle_fields"].append({"verbose_name": verbose_name, "value": value})
                break

        return context
