from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.core import serializers
from models import Guy
import json
'''Listado mediante peticiones AJAX/ barra de busqueda asincrona'''

def search(request):
    title = request.GET.get('title') #con .get accedemos a el request en forma de diccionario
    guys = Guy.objects.filter(title__startswith=title)
    guys = [guy_serializer(guy) for guy in guys] #creamos una lista de diccionarios para poder iterarlos
    return HttpResponse(json.dumps(guys), content_type='application/json')

def guy_serializer(guy):
    return {'name' : guy.name, 'age': guy.age}







