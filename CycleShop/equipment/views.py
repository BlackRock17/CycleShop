from django.apps import apps
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic as views

from CycleShop.equipment.forms import EquipmentFilterForm, TypeEquipmentFilterForm
from CycleShop.equipment.models import Equipment


class EquipmentsListView(views.ListView):
    template_name = "equipments/equipments_list.html"
    paginate_by = 20
    context_object_name = "equipment_list"

    def get_queryset(self):
        queryset = Equipment.objects.all()
        form = EquipmentFilterForm(self.request.GET)
        if form.is_valid():
            category = form.cleaned_data['category']
            if category:
                self.request.GET = self.request.GET.copy()
                self.request.GET['category'] = category
                return queryset
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EquipmentFilterForm(self.request.GET)
        return context

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        form = EquipmentFilterForm(request.GET)
        if form.is_valid():
            category = form.cleaned_data['category']
            if category:
                return redirect(reverse('equipment_category_list', kwargs={'category': category}))
        return super().get(request, *args, **kwargs)


class EquipmentCategoryListView(views.ListView):
    template_name = "equipments/equipment_category_list.html"
    paginate_by = 20
    context_object_name = "equipment_list"

    def get_queryset(self):
        category = self.kwargs['category']
        model = apps.get_model('equipment', category)

        if model:
            queryset = model.objects.all()
            form = TypeEquipmentFilterForm(category, self.request.GET)

            if form.is_valid():
                category_filter = form.cleaned_data.get('category')
                size_filter = form.cleaned_data.get('size')

                if category_filter:
                    queryset = queryset.filter(category=category_filter)
                if size_filter:
                    queryset = queryset.filter(size=size_filter)
        else:
            queryset = Equipment.objects.none()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs['category']
        context['category'] = category
        context['form'] = TypeEquipmentFilterForm(category, self.request.GET)
        return context
