from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def initiative(request):
    return render(request, 'initiative.html')

def innovativeness(request):
    return render(request, 'innovativeness.html')

def perseverance(request):
    return render(request, 'perseverance.html')

def conscientiousness(request):
    return render(request, 'conscientiousness.html')

def problemsolving(request):
    return render(request, 'problemsolving.html')
