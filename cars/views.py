from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from  cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView
from babel.numbers import format_currency




class CarsListView(ListView):

    model = Car # model que esta-rá sendo usado
    template_name = 'cars.html' # Faz a mesma função que o render, só precisa informar qual o template que será renderizado
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        
        if search:
            cars = cars.filter(model__icontains=search)

        for car in cars:
            car.fomatted_value = format_currency(car.value, 'BRL', locale='pt_BR')

        return cars



class NewCarCreateView(CreateView):
    model = Car # Informar qual o model
    form_class = CarModelForm # De qual form virá os dados 
    template_name = 'new_car.html' # em qual template está localizado esse formulário
    success_url = '/cars/' # para qual URL será direcionado após o cadastro ter êxito
    

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'