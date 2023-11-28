from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import viewsets, permissions

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    # the main query for the INDEX route
    queryset = Todo.objects.all()
    # the serializer class for serializing output
    serializer_class = TodoSerializer
    # optional permission class, sets permission level
    permission_classes =  [permissions.AllowAny] #Could be [permissions.IsAuthenticated]
    
