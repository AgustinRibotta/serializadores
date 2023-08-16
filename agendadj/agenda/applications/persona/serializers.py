# Rest
from rest_framework import serializers, pagination
# Models 
from .models import (
    Person,
    Reunion,
    Hooby,
)


# Indicamos los componetes que queremos que nos liste el serializador
class PersonSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = ('__all__')
        
   
# Generar serializers que no dependan de un modelo      
class PersonaSerializers(serializers.Serializer):
    
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    # De esta manera agregamos un atributo que no tiene el modelo
    activo = serializers.BooleanField(default=False)
    # De esta manera agregamos un atributo que no tiene el modelo y lo mostramos cuando se agregue
    online = serializers.BooleanField(required=False)
    

# Indicamos los componetes que queremos que nos liste el serializador
class Persona2Serializers(serializers.ModelSerializer):
    
    # De esta manera podemos agregar atributos que no estan en el modelo
    online = serializers.BooleanField(default=False)
    
    class Meta:
        model = Person
        fields = ('__all__')
        
 
# De esta manera serializamos una relaicon ForeignKEy       
class ReunionSerializer(serializers.ModelSerializer):
    
    perosna = PersonSerializers()
    
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fehca',
            'hora',
            'asunto',
            'perosna',
        )


#  Serializamos el modelo Hooby
class HoobySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Hooby
        fields = ('__all__')
        


# De esta manera serializamos una relaicon ManyToManyField   
class Person1Serializers(serializers.ModelSerializer):
    
    hobbies = HoobySerializers(many = True)
    
    class Meta:
        model = Person
        fields = (
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            )


# De esta manera podemos aplicar methodos a nuestros serializadores
class ReunionSerializer1(serializers.ModelSerializer):
    
    fecha_hora = serializers.SerializerMethodField()
    
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fehca',
            'hora',
            'asunto',
            'perosna',
            'fecha_hora'
        )
    
    def get_fecha_hora(self, obj):
        return f'{obj.fehca} {obj.fehca}'
        

# De esta manera serializamos una relaicon ForeignKEy y ManyToManyField   
class ReunionSerializer2(serializers.ModelSerializer):
    
    perosna = Person1Serializers()
    
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fehca',
            'hora',
            'asunto',
            'perosna',
        )


# Serializador con un link a  nuestra relacion ForeignKEy
class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fehca',
            'hora',
            'asunto',
            'perosna',
        )
        extra_kwargs = {
            'perosna' : {
                'view_name' : 'perona_app:detalle',
                'lookup_field' : 'pk'
            }
        }
    
        
# Serialziador de paginacion
class PersonPaginationSerializer(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100
    
    
class CountReunionJobSerializers(serializers.Serializer):
    
    perosna__job = serializers.CharField()
    cantidad = serializers.IntegerField()

