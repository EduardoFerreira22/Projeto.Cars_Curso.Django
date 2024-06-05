from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #fORMULÁRIOS DE AUTENTICAÇÃO PRONTOS 
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.

def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})

def login_view(request):
    if request.method == "POST":
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('cars_list')
    else:
        login_form = AuthenticationForm()
    return render(request, "login.html", {"login_form": login_form})


def logout_view(request):
    logout(request)
    return redirect('cars_list')