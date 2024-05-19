from django.shortcuts import render, redirect
from django.http import HttpResponse
from  cars.models import Car
from cars.forms import CarModelForm

# Create your views here.
def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search') #pega os dados do usuário através do parâmetro 'search' e armazena na variável.
    
    if search:# verifica se o usuário fez alguma busca
        cars = Car.objects.filter(model__icontains=search).order_by('model') #pucha os objetos do banco de dados através do metódo 'filter' e trazendo tudo que contain.

    return render(
        request,
        'cars.html', 
        {'cars': cars} # caso o usuário não tenha feito nenhuma busca o programa vai trazer todos os carros.
    )

def new_car_view(request):
    if request.method == 'POST':
        #instância o CarModelForm
        new_car_form = CarModelForm(request.POST, request.FILES)# REQUEST.FILES PARA CASO A REQUISIÇÃO TRAGA IMAGENS
        
        if new_car_form.is_valid(): # valida os dados
            new_car_form.save() # metodo dentro do form
            return redirect('cars_list')
        else:
            pass
    else:
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})