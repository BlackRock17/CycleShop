from django.views import generic as views


class HomePageView(views.TemplateView):
    template_name = "common/home_page.html"

