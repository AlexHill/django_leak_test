from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.

def leaky_view(request):
    return TemplateResponse(request, ['missing.html', 'present.html'])

def safe_view(request):
    return TemplateResponse(request, ['present.html', 'missing.html'])

