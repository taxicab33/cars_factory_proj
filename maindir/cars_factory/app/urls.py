from django.urls import path
from .views import *

urlpatterns = [
    path('', CarsListView.as_view()),
]