from django.views import generic as views

from CycleShop.accessories.models import Category


class HomePageView(views.TemplateView):
    template_name = "common/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accessories_categories'] = Category.choices
        return context

