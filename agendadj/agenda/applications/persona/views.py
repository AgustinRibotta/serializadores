# Django
from django.shortcuts import render

# Rest 
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
# Models
from .models import(
    Person,
    Reunion,
)
# Serializers
from .serializers import (
    PersonSerializers,
    PersonaSerializers,
    Persona2Serializers,
    ReunionSerializer,
    Person1Serializers,
    ReunionSerializer1,
    ReunionSerializer2,
    ReunionSerializerLink,
    PersonPaginationSerializer,
    CountReunionJobSerializers,
)


# Listado de personas
class PersonListAPIView(ListAPIView):
    
    serializer_class = PersonSerializers
    
    def get_queryset(self):
        return Person.objects.all()


# Listado de personas relaicon ManyToManyField
class Person1ListAPIView(ListAPIView):
    
    serializer_class = Person1Serializers
    
    def get_queryset(self):
        return Person.objects.all()


# Registrar personas
class PersonCreateAPIView(CreateAPIView):
    
    serializer_class = PersonSerializers
    

# Detalles personas
class PersonRetrieveAPIView(RetrieveAPIView):
    
    serializer_class = Person1Serializers    
    # Le indicamos donde queremos que busque la informacion
    queryset = Person.objects.all()
    

# Delete persona
class PersonDestroyAPIView(DestroyAPIView):
    
    serializer_class = PersonSerializers
    # Le indicamos donde queremos que busque la informacion
    queryset = Person.objects.all()
    

# Actualizar persona
class PersonUpdateAPIView(UpdateAPIView):
    
    serializer_class = PersonSerializers  
    # Le indicamos donde queremos que busque la informacion
    queryset = Person.objects.all()


# Actualizar persona trayendo datos anteriores
class PersonURetrieveUpdateAPIView(RetrieveUpdateAPIView):
    
    serializer_class = PersonSerializers  
    # Le indicamos donde queremos que busque la informacion
    queryset = Person.objects.all()


# Actualizar persona trayendo datos anteriores y te permite eliminar
class PersonURetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = PersonSerializers  
    # Le indicamos donde queremos que busque la informacion
    queryset = Person.objects.all()


# Listado de personas con serialaizer que no depende a un modelo
class PersonaListAPIView(ListAPIView):
    
    serializer_class = PersonaSerializers
    
    def get_queryset(self):
        return Person.objects.all()


# Listado de personas con serialaizer que no depende a un modelo y agregamos atributos
class Persona2ListAPIView(ListAPIView):
    
    serializer_class = Persona2Serializers
    
    def get_queryset(self):
        return Person.objects.all()


# Listado de reuniones relaicon ForeignKEy   
class ReunionListAPIView(ListAPIView):
    
    serializer_class = ReunionSerializer
    
    def get_queryset(self):
        return Reunion.objects.all()


#  Listado de reuniones aplicando methodos en los serialziadores
class ReunionListAPIView1(ListAPIView):
    
    serializer_class = ReunionSerializer1
    
    def get_queryset(self):
        return Reunion.objects.all()
    

#  Listado de reuniones aplicando ForeignKEy y ManyToManyField
class ReunionListAPIView2(ListAPIView):
    
    serializer_class = ReunionSerializer2
    
    def get_queryset(self):
        return Reunion.objects.all()
    

#  Link a la relacion ForeignKEy
class ReunionListAPIViewLink(ListAPIView):
    
    serializer_class = ReunionSerializerLink
    
    def get_queryset(self):
        return Reunion.objects.all()
    

# Listado de personas con paginacion
class PersonPaginationListAPIView(ListAPIView):
    
    serializer_class = PersonSerializers
    pagination_class = PersonPaginationSerializer
    
    def get_queryset(self):
        return Person.objects.all()
    

# 
class ReunionByPersonJob(ListAPIView):
    
    serializer_class = CountReunionJobSerializers
    
    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()
    