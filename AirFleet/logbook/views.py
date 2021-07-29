from django.shortcuts import render
from rest_framework import generics
from .serializers import LogbookEntrySerializer, LogbookDetailSerializer
from .models import entry

# Create your views here.

class LogbookAPIView(generics.ListAPIView):
    queryset = entry.objects.all()
    serializer_class = LogbookEntrySerializer

class LogbookRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = entry.objects.all()
    serializer_class = LogbookDetailSerializer

class LogbookCreateAPIView(generics.CreateAPIView):
    queryset = entry.objects.all()
    serializer_class = LogbookDetailSerializer

class LogbookRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = entry.objects.all()
    serializer_class = LogbookDetailSerializer

class LogbookDestroyAPIView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = entry.objects.all()