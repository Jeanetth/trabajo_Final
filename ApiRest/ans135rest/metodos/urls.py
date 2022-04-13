from django.urls import path
from . import views

urlpatterns = [
	path('unidad1/sin/', views.sinx, name='Sinx'),
	path('unidad2/biseccion/', views.biseccion, name='Biseccion'),
]
