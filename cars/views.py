from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from  cars.models import Car
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required # Controle de autorização de usuários
from django.utils.decorators import method_decorator
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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
    
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

"""
com o method @method_decorator(login_required(login_url='login'), name='dispatch') estiver trabalhando, o usuário não conseguirá acessar essa view sem realizar o login primeiro
caso tente será redirecionado para a view 'login'.
"""
@method_decorator(login_required(login_url='login'), name='dispatch') # Faz uma verificação  nas permissões de usuários para verificar se pode executar essa view
class NewCarCreateView(CreateView):
    model = Car # Informar qual o model
    form_class = CarModelForm # De qual form virá os dados 
    template_name = 'new_car.html' # em qual template está localizado esse formulário
    success_url = '/cars/' # para qual URL será direcionado após o cadastro ter êxito
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car  #usa o model form
    form_class = CarModelForm # Pega o formulário de cadastros de produtos
    template_name = 'car_update.html' # Insere modelForm no html
    success_url = '/cars/' # se tiver sucesso redireciona para a página cars

    def get_success_url(self): # Reescrevendo uma função do Django para conseguir redirecionar o usuário para uma url personalizada após fazer um Update
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
        """
        O metódo reverse_lazy server para redirecionar o usuário após um evento
        nesse caso a função está redirecionando para a url=car_detail e pegando 
        a primary key do item alterado evitando que após realizar a edição do item
        o usuário não sejá redirecionado para a lista de carros da tela principal, 
        más sim para o template do mesmo item que foi alterado.
        Mais sobre reverse_lazy: https://docs.djangoproject.com/en/5.0/ref/urlresolvers/
        """

@method_decorator(login_required(login_url='login'), name='dispatch') 
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'