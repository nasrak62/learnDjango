from django.shortcuts import render
from .models import Feature

def index(request):
    feature1 = Feature(0, 'name1', 'details')

    context = {
        'feature'
        
    }
    return render(request, 'index.html', {'name': 'saar'})