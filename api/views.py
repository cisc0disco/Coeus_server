from django.shortcuts import render
from django.contrib.auth import authenticate, login
from home.models import HomeData
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ApiSerializer
from django.core import serializers

class ApiView(APIView):
    def post(self, request):
        serializer = ApiSerializer(request.data)

        username = serializer.data["username"]
        password = serializer.data["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:

            data = HomeData.objects.get(username=user.username)

            content = {'azure_key': data.azure_key, 'azure_end': data.azure_end, "wit_key": data.wit_key, "weather_key": data.weather_key, "bridge_ip": data.bridge_ip, "voice": data.voice}

            return Response(content)
        
        else:
            return Response("Error")