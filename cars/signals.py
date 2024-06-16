#importar funções prontas de ações
from django.db.models.signals import pre_save,post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from openai_api.client import get_car_ai_bio 

"""
Os Signals são utilizados para execurar operações antes do post(pré_save, post_save), delete ou update
onde é possível executar funções que podem ser executadas antes de criar um dado no banco de dados
ou realizar ações posteriores.
"""
def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value') #Soma todos os campos 
    )['total_value']

    CarInventory.objects.create( #No model CarInvetory, crie um registro
        cars_count= cars_count,
        cars_value= cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio: # se a instância do carro que está sendo salvo vier com a bio como none será feito
        # Passando parâmetros para que a inteligência artificial possa criar a bio do carro
        ai_bio = get_car_ai_bio(
            instance.model, instance.brand, instance.model_year
        )

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()