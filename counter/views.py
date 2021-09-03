from django.views.generic.edit import FormView
from django.shortcuts import render

def top(request):
    return render(request, 'index.html')
