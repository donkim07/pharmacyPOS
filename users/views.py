from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def users(request):
    return HttpResponse("Hello, world. You're at the users index.")