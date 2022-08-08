from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'blog/home.html')


def sobre(request):
    return HttpResponse('<h1>SOBRE</h1>')

def contato(request):
    return HttpResponse('<h1>CONTATO</h1>')