from django.views import generic as views
from .models import Accessories
from .forms import AccessoryCategoryForm


class AccessoriesListView(views.ListView):
    model = Accessories
    template_name = 'accessories/accessories_list.html'
    context_object_name = 'accessories'

    def get_queryset(self, category=None):
        queryset = super().get_queryset()
        category = category or self.kwargs.get('category')
        form = AccessoryCategoryForm(self.request.GET)
        if form.is_valid():
            selected_category = form.cleaned_data['category']
            if selected_category:
                if selected_category == 'All Categories':
                    return queryset
                else:
                    return queryset.filter(category=selected_category)
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AccessoryCategoryForm(self.request.GET)
        accessories = context['accessories']

        for accessory in accessories:
            accessory.pk_type = type(accessory.pk).__name__
        return context


class AccessoryDetailView(views.DetailView):
    model = Accessories
    template_name = 'accessories/accessory_detail.html'
    context_object_name = 'accessory'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accessory = self.get_object()
        context['accessory_fields'] = [
            {'name': field.name, 'verbose_name': field.verbose_name, 'value': getattr(accessory, field.name)}
            for field in accessory._meta.fields if field.verbose_name not in ("ID", "quantity")
        ]

        context['quantity'] = accessory.quantity

        return context
