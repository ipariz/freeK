from log.models import Log
from rest_framework import serializers

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('path', 'method', 'client_ip', 'query')