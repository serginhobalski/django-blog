from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'blog/home.html')

def sobre(request):
    return render(request, 'blog/sobre.html')

def contato(request):
    return render(request, 'blog/contato.html')