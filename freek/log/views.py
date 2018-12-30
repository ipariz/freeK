from django.shortcuts import render
from rest_framework import viewsets
from log.models import Log
from log.serializers import LogSerializer

class LogViewSet(viewsets.ModelViewSet):
    serializer_class = LogSerializer
    queryset = Log.objects.all()
