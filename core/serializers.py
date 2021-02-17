import requests
from django.contrib.redirects.models import Redirect
from rest_framework import serializers
import json

class RedirectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Redirect
        fields = '__all__'


class ShortLinkSerializer(serializers.Serializer):
    key = serializers.CharField(max_length=50, required=True)
    urls = serializers.ListField(required=True, child=serializers.CharField(max_length=100))
    # url = serializers.CharField(max_length=1000, required=True,
    #                             style={'base_template': 'textarea.html', 'rows': 10})

    def create(self, validated_data):
        return validated_data
