from django.core.exceptions import SynchronousOnlyOperation
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import response,status
from django.contrib.auth import authenticate

from rest_framework.generics import GenericAPIView

# from authetifications.serializer import RegisterSerializer, LoginSerializer

# Create your views here.
"""class Register(GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request):
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return response.Response(serializer.data, status.HTTP_201_CREATED)
    
    return response.Response(serializer.errors, status.HTTP_404_NOT_FOUND)


class Login(GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request):
    email = request.data.get('email', None)
    password = request.data.get('password', None)

    user = authenticate(username=email, password=password)

    if user:
      serializer = self.serializer_class(user)

      return response.Response(serializer.data, status.HTTP_200_OK)
    
    return response.Response({'message': 'Invalid email or password'}, status.HTTP_401_UNAUTHORIZED)
"""