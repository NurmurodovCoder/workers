from .models import Person
from .serializers import PersonSerializers
from rest_framework import generics


class PersonCreateListAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers


class PersonRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers

