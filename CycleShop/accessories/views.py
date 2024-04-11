from django.views import generic as views
from .models import Accessories
from .forms import AccessoryCategoryForm


class AccessoriesListView(views.ListView):
    model = Accessories
    template_name = "accessories/accessories_list.html"
    context_object_name = "accessories"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get("category")
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AccessoryCategoryForm(self.request.GET or None)

        for accessory in context["accessories"]:
            images = accessory.accessory_images.all()
            if images:
                accessory.first_image = images[0]
            else:
                accessory.first_image = None

        return context


class AccessoryDetailView(views.DetailView):
    model = Accessories
    template_name = "accessories/accessory_detail.html"
    context_object_name = "accessory"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accessory = self.get_object()
        context["accessory_fields"] = [
            {"name": field.name, "verbose_name": field.verbose_name, "value": getattr(accessory, field.name)}
            for field in accessory._meta.fields if field.verbose_name not in ("ID", "quantity")
        ]

        return context
