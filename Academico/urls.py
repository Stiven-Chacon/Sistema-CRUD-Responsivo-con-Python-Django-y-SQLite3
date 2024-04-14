from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicioncurso/<codigo>', views.edicioncurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
]
