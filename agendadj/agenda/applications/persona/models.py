#
from model_utils.models import TimeStampedModel
#
from django.db import models
#
from .managers import ReunionManager

# Pasa Tiempos
class Hooby(TimeStampedModel):
    
    hobby = models.CharField(
        'Pasa tiempo', 
        max_length=50
    )

    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'
    
    def __str__(self):
        return self.hobby


# Personas
class Person(TimeStampedModel):
    """  Modelo para registrar personas de una agenda  """

    full_name = models.CharField(
        'Nombres', 
        max_length=50,
    )
    job = models.CharField(
        'Trabajo', 
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        'Telefono',
        max_length=15,
        blank=True,
    )
    hobbies = models.ManyToManyField(Hooby)


    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return str(self.id) + ' ' + self.full_name


# Reunion
class Reunion(TimeStampedModel):

    perosna = models.ForeignKey(
        Person, 
        on_delete=models.CASCADE
    )
    fehca = models.DateField()
    hora = models.TimeField()
    asunto = models.CharField(
        'Asunto de Reunion',
        max_length=100
    )

    objects = ReunionManager()

    class Meta:
        verbose_name = 'Reunion'
        verbose_name_plural = 'Reunion'
    
    def __str__(self):
        return self.asunto


