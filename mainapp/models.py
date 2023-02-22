from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Person(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=10)
    # def __str__(self):
    #     return self.name





class Breed(models.Model):
    name=models.CharField(max_length=200)
    speed=models.IntegerField(default=1, validators=[MaxValueValidator(10),MinValueValidator(1)])

    def __str__(self):
        return self.name



class Pet(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=10)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    food = models.CharField(max_length=20)
                           