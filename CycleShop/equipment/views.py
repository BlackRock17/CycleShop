from django.db.models import Q
from django.views import generic as views

from CycleShop.equipment.forms import EquipmentFilterForm
from CycleShop.equipment.models import Equipment


class EquipmentsListView(views.ListView):
    model = Equipment
    template_name = "equipments/equipments_list.html"
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        form = EquipmentFilterForm(self.request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            if search_query:
                queryset = queryset.filter(
                    Q(name__icontains=search_query) |
                    Q(description__icontains=search_query)
                )
            goggles_categories = form.cleaned_data['goggles_categories']
            if goggles_categories:
                queryset = queryset.filter(goggles__category__in=goggles_categories)
            protection_categories = form.cleaned_data['protection_categories']
            if protection_categories:
                queryset = queryset.filter(protection__category__in=protection_categories)
            helmet_categories = form.cleaned_data['helmet_categories']
            if helmet_categories:
                queryset = queryset.filter(helmet__category__in=helmet_categories)
            gloves_categories = form.cleaned_data['gloves_categories']
            if gloves_categories:
                queryset = queryset.filter(gloves__category__in=gloves_categories)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EquipmentFilterForm(self.request.GET)
        return context
