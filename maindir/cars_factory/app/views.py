from django.views.generic import ListView
from .models import *


class CarsListView(ListView):
    model = Car
    template_name = 'app/cars_list.html'
    context_object_name = 'cars'
