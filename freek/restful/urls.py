from django.conf.urls import url, include
from rest_framework import routers
from restful import views

router = routers.DefaultRouter()
router.register(r'pizza', views.PizzaViewSet)
router.register(r'topping', views.ToppingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]