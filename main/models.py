from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.FloatField()

    def __str__(self):
        return self.name
