from django.db import models


#Modelos de  carros
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Categorias de carros
class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.description
    
#Tabela de dados dos carros
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') #Modelo
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, related_name='car_category', null=True)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10,blank=True, null=True) #campo que recebe a placa do carro
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True,null=True) #Campo de uploads de imagens
    """
        blank=true permite deixar um campo em branco sem necessidade de preenchimento.
    """
    def __str__(self):
        return self.model 
    #muda o padrão de mostrar o título "Objects num" por modelo do e número do objeto na página de Adm

