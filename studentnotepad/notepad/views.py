from rest_framework import generics
from django.shortcuts import render
from .models import Student, Note
from .serializers import StudentSerializer, NoteSerializer



class StudentListCreateApiView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class NoteListCreateApiView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer    


class StudentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class NoteDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer




#class StudentDeleteApiView(generics.DestroyAPIView):
    #queryset = Student.objects.all()
   # serializer_class = StudentSerializer

#class NoteDeleteApiView(generics.DestroyAPIView):
  #  queryset = Note.objects.all()
 #   serializer_class = NoteSerializer
