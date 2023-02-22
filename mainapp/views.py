# from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mainapp.serializers import PeopleSerializer
from .models import Person
from rest_framework import viewsets


