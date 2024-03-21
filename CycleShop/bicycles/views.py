from django.db import models
from django.shortcuts import render
from django.views import generic as views

from CycleShop.bicycles.forms import BicycleFilterForm
from CycleShop.bicycles.models import MountainBicycle, RoadBicycle, ElectricBicycle, Bicycle


class BicycleListView(views.ListView):
    template_name = 'bicycle_list.html'
    context_object_name = 'bicycles'
    paginate_by = 20

    def get_queryset(self):
        category = self.kwargs['category']
        queryset = self.get_bicycle_queryset(category)

        form = BicycleFilterForm(category, self.request.GET)
        if form.is_valid():
            filters = {
                key: value for key, value in form.cleaned_data.items() if value
            }
            queryset = queryset.filter(**filters)

        return queryset

    @staticmethod
    def get_bicycle_queryset(category):
        if category == 'mountain':
            return MountainBicycle.objects.all()
        elif category == 'road':
            return RoadBicycle.objects.all()
        elif category == 'electric':
            return ElectricBicycle.objects.all()
        else:
            return MountainBicycle.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BicycleFilterForm(self.kwargs['category'], self.request.GET)
        return context


class BicycleDetailView(views.DetailView):
    model = Bicycle
    template_name = 'bicycle_detail.html'
    context_object_name = 'bicycle'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bicycle = self.get_object()
        context['bicycle_fields'] = []

        for field in bicycle._meta.get_fields():
            if not field.name.startswith('_') and field.name != 'images':
                if isinstance(field, models.OneToOneRel):
                    # Skip OneToOneRel fields
                    continue
                elif field.is_relation:
                    context['bicycle_fields'].append({
                        'name': field.name,
                        'verbose_name': field.related_model._meta.verbose_name,
                        'value': getattr(bicycle, field.name, None),
                        'is_relation': True,
                    })
                else:
                    context['bicycle_fields'].append({
                        'name': field.name,
                        'verbose_name': field.verbose_name,
                        'value': getattr(bicycle, field.name, None),
                        'is_relation': False,
                    })

        return context
