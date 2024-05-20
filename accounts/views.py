from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.

def register_view(request):
    user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})
