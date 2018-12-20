from restful.models import Pizza, Topping
from rest_framework import serializers

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('salad', 'soda', 'yogurt') #'__all__'

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('type', 'toppings') #'__all__'
    