from django.contrib.redirects.models import Redirect
from rest_framework import serializers


class RedirectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Redirect
        fields = '__all__'