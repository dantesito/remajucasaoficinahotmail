from django.shortcuts import render
from django.http import HttpResponse
from decouple import config

def joder(request):
    return HttpResponse(config("USUARIO"))