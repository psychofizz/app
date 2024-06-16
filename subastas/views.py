from django.shortcuts import render        
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from subastas.serializer import *

        
def about(request):    
    return HttpResponse('<h1>This is not at all about me!.</h1>')  

@api_view([ 'GET'])
def getData (request) :
    person = {'name': 'Dennis', 'age' :28}
    return Response(person)

@api_view(['POST'])
def register_new_user (request):
    data = {
        'user_id': request.data.get('user_id'),
        'first_name': request.data.get('first_name'),
        'second_name': request.data.get('second_name'),
        'first_surname': request.data.get('first_surname'),
        'second_surname': request.data.get('second_surname'),
        'user_dni': request.data.get('user_dni'),
        'user_address': request.data.get('user_address'),
        'verification': request.data.get('verification'),
        'user_type': request.data.get('user_type'),
        'picture': request.data.get('picture'),
        'payment_method': request.data.get('payment_method')
    }
    serializer = UserSerializer(data=data)
    print(serializer.is_valid())
    print(serializer.errors)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(status.HTTP_400_BAD_REQUEST)