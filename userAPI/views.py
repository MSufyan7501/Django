from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
# from imagesss import 

class TextView(APIView):
    def get(self, request, format=None):
        print('API Was called')
        return Response('Shukar ha ',status=200)
