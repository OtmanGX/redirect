from django.contrib.redirects.models import Redirect
# Create your views here.
from rest_framework import viewsets, filters
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers import RedirectSerializer, ShortLinkSerializer
import urllib
import requests
class RedirectView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['old_path', 'new_path']
    filter_fields = '__all__'
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializer


class Cuttly(CreateAPIView):

    serializer_class = ShortLinkSerializer

    def get(self, request, *args, **kwargs):
        return Response({})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.data)
        data = serializer.data
        res = [self.shorten(data['key'], urllib.parse.quote(url))
               for url in data['urls']]
        return Response(res)

    def shorten(self, key, url):
        r = requests.get('http://cutt.ly/api/api.php?key={}&short={}'
                         .format(key, url))
        # print(r.json()['url']['shortLink'])
        return r.json()['url']['shortLink']



    # def post(self):
    #     return Response({})
    # def get(self, request, *args, **kwargs):
    #     r = requests.get('http://cutt.ly/api/api.php?key={}&short={}'
    #                      .format(request.GET['key'], request.GET['url']))
    #     return Response(r.json())

#
# r = requests.get('http://cutt.ly/api/api.php?key={}&short={}'
#                      .format(validated_data['key'], validated_data['url']))
#         res = validated_data
#         print(r.json()['url']['shortLink'])
#         res['shortLink'] = r.json()['url']['shortLink']