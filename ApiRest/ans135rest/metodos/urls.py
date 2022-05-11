from django.urls import path
from . import views

urlpatterns = [
	# url's para método de la unidad 1
	path('unidad1/sin/', views.sinx, name='Sinx'),
	path('unidad1/cos/', views.cosx, name='Cosx'),
	path('unidad1/cosh/', views.coshx, name='Coshx'),
	#url's para métodos de la unidad 2
	path('unidad2/biseccion/', views.biseccion, name='Biseccion'),
	path('unidad2/falsaposicion/', views.falsaPosicion, name='Falsa Posicion'),
	path('unidad2/puntofijo/', views.puntoFijo, name='Punto Fijo'),
	path('unidad2/newtonraphson/', views.newtonRaphson, name='Newton Raphson'),
	path('unidad2/bairstow/', views.bairstow, name='Bairstow'),
	#url's para método de la unidad 3
]
