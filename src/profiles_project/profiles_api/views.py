from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        an_apiview = [
        'uses HTTP Methods as function(get, Post, Put, Patch Delete)',
        'Similar to traditional django Views',
        'Mapped Manually To Urls',
        ]
        return Response({'message':'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name= serializer.data.get('name', 'imei')
            imei= serializer.data.get('imei')

            message = 'Hello: {} and imei: {}'.format(name, imei)
            return Response({'message':message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
            return Response({'method': 'put'})

    def patch(self, request, pk=None):
            return Response({'method': 'patch'})

    def delete(self, request, pk=None):
            return Response({'method': 'delete'})
