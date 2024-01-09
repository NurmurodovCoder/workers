from .models import Person
from .serializers import PersonSerializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import PersonDetailPermission


class PersonCreateListAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
    permission_classes = IsAuthenticated


class PersonRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
    permission_classes = PersonDetailPermission

