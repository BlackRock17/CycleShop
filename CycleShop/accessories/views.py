from django.views import generic as views
from CycleShop.accessories.forms import AccessoryCategoryForm
from CycleShop.accessories.models import Accessories, Category


from django.views import generic as views
from .models import Accessories, Category
from .forms import AccessoryCategoryForm


class AccessoriesListView(views.ListView):
    model = Accessories
    template_name = 'accessories/accessories_list.html'
    context_object_name = 'accessories'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.kwargs.get('category')
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
        return context
