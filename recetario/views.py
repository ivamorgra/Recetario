from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Receta
# Create your views here.

def index(request):
    recipes = Receta.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def users_list(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def recipes_list(request):
    recipes = Receta.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})