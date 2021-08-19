from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    foods = Food.objects.all()
    form = FoodForm()
    totalCalories = 0
    totalCarbs = 0
    totalFats = 0
    totalProtein = 0
    for food in foods:
        totalCalories += food.calories
        totalCarbs += food.carbs
        totalFats += food.fats
        totalProtein += food.protein
    context = {
        'foods': foods,
        'form': form,
        'totalCalories': totalCalories,
        'totalProtein': totalProtein,
        'totalFats': totalFats,
        'totalCarbs': totalCarbs,
    }
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'main/home.html', context)

def updateFood(request, pk):
    food = Food.objects.get(id=pk)
    form = FoodForm(instance=food)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'main/update_food.html', context)

def deleteFood(request, pk):
    food = Food.objects.get(id=pk)
    context = {
        'food': food
    }
    if request.method == 'POST':
        food.delete()
        return redirect('/')
    return render(request, 'main/delete.html', context)
