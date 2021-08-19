from django import forms
from django.forms import ModelForm
from .models import *


class FoodForm(forms.ModelForm):
    name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add new food...'}))
    quantity = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add quantity...'}))
    carbs = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add carb amount...'}))
    protein = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add protein amount...'}))
    fats = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add total fats...'}))
    calories = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add calories...'}))
    class Meta:
        model = Food
        fields = '__all__'
