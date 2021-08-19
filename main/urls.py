from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('update_food/<str:pk>/', views.updateFood, name = "update_food"),
    path('delete/<str:pk>/', views.deleteFood, name = "delete"),
]
