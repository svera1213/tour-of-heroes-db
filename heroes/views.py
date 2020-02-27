from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from heroes.models import Hero

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_heroes(request):
    data = Hero.objects.all()
    qs_json = serializers.serialize('json', data)
    return HttpResponse(qs_json, content_type='application/json')