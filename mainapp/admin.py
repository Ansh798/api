from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name','age']

admin.site.register(Breed)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id','name']