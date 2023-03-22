from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home),
    path('registrarCurso/', views.registrarCurso),
    path('editarCurso/<codigo>', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('edicionCurso/', views.edicionCurso)
]