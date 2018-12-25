from django.db import models

class Log(models.Model):
    path = models.TextField()
    method = models.CharField(max_length=10)
    client_ip = models.GenericIPAddressField()
    query = models.TextField()
