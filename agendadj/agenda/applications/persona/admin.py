from django.contrib import admin

from .models import (
    Person,
    Hooby,
    Reunion
)

admin.site.register(Person)
admin.site.register(Hooby)
admin.site.register(Reunion)
