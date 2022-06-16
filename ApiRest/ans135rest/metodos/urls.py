from django.urls import path
from . import views

urlpatterns = [
	#url's para métodos de la unidad 1
	path('unidad1/sin/', views.sinx, name='Sinx'),
	path('unidad1/cos/', views.cosx, name='Cosx'),
	path('unidad1/cosh/', views.coshx, name='Coshx'),
	path('unidad1/arctgx/',views.arctgx, name='Arctgx'),
	path('unidad1/fraccion/',views.fraccion, name='Fraccion'),
	path('unidad1/ln/', views.logaritmo, name="Logaritmo"),
	path('unidad1/arcsin/', views.arcsinx, name="Arcsinx"),
	path('unidad1/sinh/', views.sinhx, name="Sinhx"),
	#url's para métodos de la unidad 2
	path('unidad2/biseccion/', views.biseccion, name='Biseccion'),
	path('unidad2/falsaposicion/', views.falsaPosicion, name='Falsa Posicion'),
	path('unidad2/puntofijo/', views.puntoFijo, name='Punto Fijo'),
	path('unidad2/newtonraphson/', views.newtonRaphson, name="Newton Raphson"),
	path('unidad2/bairstow/', views.bairstow, name="Bairstow"),
	path('unidad2/muller/',views.muller, name="Muller"),
	path('unidad2/secante/', views.secante, name="Secante"),
	#url's para métodos de la unidad 3
	path('unidad3/lagrange/', views.lagrange, name="Lagrange"),
	path('unidad3/diferenciasdivididas/', views.diferencias_divididas, name="Diferencias Divididas"),
	path('unidad3/newton/', views.interpolacion_newton, name="Interpolacion de Newton"),
	path('unidad3/hermite/', views.hermite, name="Hermite"),
	#url's para metodos de la undiad 4
	path('unidad4/derivacion/', views.derivacion, name="Derivacion"),
	path('unidad4/richardson/', views.richardson, name="Richardson"),
	path('unidad4/integracion/', views.integracion, name="Integracion"),
	path('unidad4/rosemberg/', views.rosemberg, name="Rosemberg"),
	#url's para metodos de la unidad 5
	path('unidad5/euler/', views.euler, name="Euler"),
	path('unidad5/taylor/', views.taylor, name="Taylor"),
	path('unidad5/rungekutta/', views.rungekutta, name="Runge Kutta"),
	path('unidad5/adaptativo/', views.adaptativo, name="Adaptativo"),
]