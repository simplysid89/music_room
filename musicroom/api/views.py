from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Define a class called "RoomView" that inherits from the "generics.CreateAPIView" class.
# This class is used to handle the creation of new instances of the "Room" model.
class RoomView(generics.ListAPIView):
    queryset= Room.objects.all()
    serializer_class=RoomSerializer