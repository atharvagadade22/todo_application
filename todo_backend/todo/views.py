from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

# Define a viewset for the Todo model
class TodoViewSet(viewsets.ModelViewSet):
    # Specify the queryset to be used for this viewset
    queryset = Todo.objects.all()
    # Specify the serializer class to be used for this viewset
    serializer_class = TodoSerializer
