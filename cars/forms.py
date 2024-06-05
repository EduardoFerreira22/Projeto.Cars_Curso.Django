from typing import Any
from django import forms
from cars.models import Brand, Car


# a criação do form deve conter todos os campos do model e tipo de dado
class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all()) #ModelChoiceField para trabalhar com campos do model que contenha chaves estrangeiras ligando outras tabelas
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    Value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Car(
            #instância os dados recebidos do form dentro da variável car e cria o car
            model = self.cleaned_data['model'], # self vem significado o CarForm()
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save() # salva na database
        return car #retorna objeto criado
    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 10000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$20.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        model_year = self.cleaned_data.get('model_year')
        if factory_year and factory_year < 1980:
            self.add_error('factory_year', 'Só é possível cadastrar carros de ano de fabricação anterior a 1980.')
        if model_year and model_year < 1980:
            self.add_error('model_year', 'Só é possível cadastrar carros de ano de modelo anterior a 1980.')
        return factory_year