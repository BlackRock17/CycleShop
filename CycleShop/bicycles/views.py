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
    queryset = Bicycle.objects.select_related('mountainbicycle', 'roadbicycle', 'electricbicycle')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bicycle = self.get_object()

        context['images'] = bicycle.images.all()

        base_fields = ['name', 'description', 'frame', 'fork', 'brakes', 'gears', 'tyres_size', 'weight', 'color',
                       'price', 'size']

        context['bicycle_fields'] = []
        for field_name in base_fields:
            verbose_name = Bicycle._meta.get_field(field_name).verbose_name
            context['bicycle_fields'].append({
                'name': field_name,
                'verbose_name': verbose_name,
                'value': getattr(bicycle, field_name, None),
                'is_relation': False,
            })

        specific_model = None
        if hasattr(bicycle, 'mountainbicycle'):
            specific_model = bicycle.mountainbicycle
            specific_fields = ['fork_travel', 'frame_travel', 'suspension_lockout', 'dropper_post', 'tubeless_ready',
                               'category']
        elif hasattr(bicycle, 'roadbicycle'):
            specific_model = bicycle.roadbicycle
            specific_fields = ['handlebar_type', 'frame_geometry', 'category']
        elif hasattr(bicycle, 'electricbicycle'):
            specific_model = bicycle.electricbicycle
            specific_fields = ['engine', 'battery', 'display', 'charger', 'motor_power', 'max_speed', 'category']

        if specific_model:
            for field_name in specific_fields:
                field = specific_model._meta.get_field(field_name)
                verbose_name = field.verbose_name
                context['bicycle_fields'].append({
                    'name': field_name,
                    'verbose_name': verbose_name,
                    'value': getattr(specific_model, field_name, None),
                    'is_relation': False,
                })

        return context
