from django.db import models

class Topping(models.Model):
    soda = models.BooleanField()
    salad = models.BooleanField()
    yogurt = models.BooleanField()

class Pizza(models.Model):
    type = models.CharField(max_length=40)
    toppings = models.ManyToManyField(Topping)