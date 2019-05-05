from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""
    def get(self, request, format=None):

        an_apiview = [
        'uses HTTP Methods as function(get, Post, Put, Patch Delete)',
        'Similar to traditional django Views',
        'Mapped Manually To Urls',
        ]
        return Response({'message':'Hello', 'an_apiview': an_apiview})
