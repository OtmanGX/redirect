from django.contrib.redirects.models import Redirect
# Create your views here.
from rest_framework import viewsets, filters

from core.serializers import RedirectSerializer


class RedirectView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['old_path', 'new_path']
    filter_fields = '__all__'
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializer
