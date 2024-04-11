from django.views import generic as views
from CycleShop.accessories.models import Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Order


class HomePageView(views.TemplateView):
    template_name = "common/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accessories_categories"] = Category.choices
        return context


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})


def handler404(request, exception):
    return render(request, '404.html', status=404)


