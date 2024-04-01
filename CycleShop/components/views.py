from django.shortcuts import render
from django.views import generic as views

from CycleShop.components.forms import ComponentFilterForm
from CycleShop.components.models import Components


class ComponentsListView(views.ListView):
    model = Components
    template_name = "components/components_list.html"
    context_object_name = "components"

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(type=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComponentFilterForm(self.request.GET or None)

        for component in context['components']:
            images = component.components_images.all()
            if images:
                component.first_image = images[0]
            else:
                component.first_image = None

        return context


class ComponentDetailView(views.DetailView):
    model = Components
    template_name = 'components/component_detail.html'
    context_object_name = 'component'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        component = self.object
        component_fields = []
        for field in component._meta.fields:
            if field.name not in ['id', 'quantity']:
                component_fields.append({
                    'name': field.name,
                    'verbose_name': field.verbose_name,
                    'value': getattr(component, field.name),
                })

        context['component_fields'] = component_fields
        context['quantity'] = component.quantity

        return context
