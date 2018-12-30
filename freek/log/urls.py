from django.conf.urls import url, include
from rest_framework import routers
from log import views

router = routers.DefaultRouter()
router.register(r'', views.LogViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]