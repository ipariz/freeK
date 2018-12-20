from django.shortcuts import render
from restful.models import Pizza, Topping
from restful.serializers import PizzaSerializer, ToppingSerializer
from rest_framework import viewsets

class PizzaViewSet(viewsets.ModelViewSet):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()

class ToppingViewSet(viewsets.ModelViewSet):
    serializer_class = ToppingSerializer
    queryset = Topping.objects.all()
    