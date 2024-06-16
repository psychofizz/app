from django.shortcuts import render        
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
        
def about(request):    
    return HttpResponse('<h1>This is not at all about me!.</h1>')  

def hentai(request):
    return HttpResponse('<h2>hell yeah milkshu!</h2>')

@api_view([ 'GET'])
def getData (request) :
    person = {'name': 'Dennis', 'age' :28}
    return Response(person)