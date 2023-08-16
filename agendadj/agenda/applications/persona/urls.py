# Django
from django.urls import path, re_path, include
# Views
from . import views

app_name = 'perona_app'

urlpatterns = [
    # Person
    path(
        'api/person/lsit/',
        views.PersonListAPIView.as_view(),
    ),
    path(
        'api/person1/lsit/',
        views.Person1ListAPIView.as_view(),
    ),
    path(
        'api/person/register/',
        views.PersonCreateAPIView.as_view(),
    ),
    path(
        'api/person/detail/<pk>/',
        views.PersonRetrieveAPIView.as_view(),
        name= 'detalle'
    ),
    path(
        'api/person/delete/<pk>/',
        views.PersonDestroyAPIView.as_view(),
    ),
    path(
        'api/person/update/<pk>/',
        views.PersonUpdateAPIView.as_view(),
    ),
    path(
        'api/person/modificar/<pk>/',
        views.PersonURetrieveUpdateAPIView.as_view(),
    ),
    path(
        'api/person/update/delete/<pk>/',
        views.PersonURetrieveUpdateDestroyAPIView.as_view(),
    ),
    # Serialaizer que no depende de un modelo
    path(
        'api/persona/lsit/',
        views.PersonaListAPIView.as_view(),
    ),
    path(
        'api/persona2/lsit/',
        views.Persona2ListAPIView.as_view(),
    ),
    # Reuniones
    path(
        'api/reunion/lsit/',
        views.ReunionListAPIView.as_view(),
    ),
    path(
        'api/reunion1/lsit/',
        views.ReunionListAPIView1.as_view(),
    ),
    path(
        'api/reunion2/lsit/',
        views.ReunionListAPIView2.as_view(),
    ),
    path(
        'api/reunionlinks/lsit/',
        views.ReunionListAPIViewLink.as_view(),
    ),
    # Paginacion
    path(
        'api/person/paginacion/',
        views.PersonPaginationListAPIView.as_view(),
    ),
    # Consultas especificas en la ORM
    path(
        'api/reunion/job/',
        views.ReunionByPersonJob.as_view(),
    ),
]

