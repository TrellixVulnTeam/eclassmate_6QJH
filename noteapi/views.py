from django.shortcuts import render
from rest_framework import viewsets

from .models import Note
from .serializers import NoteSerializers

class NoteSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializers
    queryset = Note.objects.all()