from rest_framework import  serializers
from .models import *

class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields=['name', 'age','id' ]





class Dogbreed(serializers.ModelSerializer):
    class Meta:
        model =Breed
        fields='__all__'


class Petserializer(serializers.ModelSerializer):
    class Meta:
        model=Pet
        fields='__all__'
