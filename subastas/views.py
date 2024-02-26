from django.shortcuts import render        
from django.http import HttpResponse
        
def about(request):    
    return HttpResponse('<h1>This is not at all about me!.</h1>')  