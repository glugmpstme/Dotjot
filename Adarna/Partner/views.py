from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def partner(request):
    template = loader.get_template('Partner/ngo.html')
    return HttpResponse(template.render(request))


