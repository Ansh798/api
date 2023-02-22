# from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from mainapp.serializers import *
from rest_framework import viewsets
from mainapp.models import *

class GetViewSet(viewsets.ViewSet):

    @action(methods=['GET'], detail=False)
    def Ansh(self, request):
        a=Person.objects.all()
        ser=PeopleSerializer(a,many=True)
        return Response(ser.data)
    
    
    def list(self, request):
            a=Breed.objects.all()
            ser=Dogbreed(a,many=True)
            return Response(ser.data)
    
    



    @action(methods=['POST'], detail=False)
    def addbreed(self,request):
        # for getting the data from the body, we need 
         data=request.data
         ser = Dogbreed(data=data)
         if ser.is_valid():
              ser.save()
              context = {
                   "msg": "Breed added successfully!"
              }
              return Response(context)
         else:
            context = {
                   "msg" : ser.errors
              }
            return Response(context)  
         
    

    
