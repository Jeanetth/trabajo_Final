from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# =========== UNIDAD 1 ==========
from metodos.unidad1.sinx import Sinx
from metodos.unidad1.cosx import Cosx
from metodos.unidad1.coshx import Coshx
from metodos.unidad1.arctgx import Arctgx
from metodos.unidad1.fraccion import Fraccion
from metodos.unidad1.sinhx import Sinhx
from metodos.unidad1.lnx import Lnx
from metodos.unidad1.arcsinx import Arcsinx
# =========== UNIDAD 2 ==========
from metodos.unidad2.biseccion import Biseccion
from metodos.unidad2.falsa_posicion import FalsaPosicion
from metodos.unidad2.punto_fijo import PuntoFijo
from metodos.unidad2.newton_raphson import Newton_Raphson
from metodos.unidad2.bairstow import Bairstow
from metodos.unidad2.muller import Muller
from metodos.unidad2.secante import Secante
#=============== UNIDAD 3 ==================
from metodos.unidad3.lagrange import Lagrange
from metodos.unidad3.diferencias_divididas import DiferenciasDivididas
from metodos.unidad3.Interpolacion_de_Newton import InterpolacionNewton
from metodos.unidad3.hermite import Hermite
#=============== UNIDAD 4 ==================
from metodos.unidad4.Derivacion import Diferenciacion
from metodos.unidad4.Richardson import Richardson
from metodos.unidad4.Integracion import Integracion
from metodos.unidad4.Rosemberg import Rosemberg
#=============== UNIDAD 5 ==================
from metodos.unidad5.euler import Euler
from metodos.unidad5.taylor import Taylor
from metodos.unidad5.rungekutta import RungeKutta


@api_view(['POST'])
def sinx(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = 'Ingresa un número positivo en las cifras significativas'
			return Response(resultado,status = status.HTTP_400_BAD_REQUEST)
		x = float(request.data['x'])
		resultado = Sinx(cifras,x).sinx
		return Response(resultado, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado,status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def cosx(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = 'Ingrese un número positivo en las cifras significativas'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		x = float(request.data['x'])
		resultado = Cosx(x,cifras).cosx
		return Response(resultado, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def coshx(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = 'Ingrese un número positivo en las cifras significativas'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		x = float(request.data['x'])
		resultado = Coshx(x,cifras).coshx
		return Response(resultado, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def arctgx(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = 'Ingrese un número positivo en las cifras significativas'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		x = float(request.data['x'])

		if x > -1 and x < 1:
			resultado = Arctgx(x,cifras).arctgx
			return Response(resultado, status=status.HTTP_200_OK)
		else:
			resultado['error'] = "El valor de x debe pertenecer al intervalo ]-1;1["
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def fraccion(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = 'Ingrese un número positivo en las cifras significativas'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		x = float(request.data['x'])

		if x > -1 and x < 1:
			resultado = Fraccion(x,cifras).fraccion
			return Response(resultado, status=status.HTTP_200_OK)
		else:
			resultado['error'] = "El valor de x debe pertenecer al intervalo ]-1;1["
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logaritmo(request):
	resultado = {}
	try:
		x = float(request.data['x'])
		cifras = int(request.data['cifras'])

		if cifras < 1:
			resultado['error'] = 'Ingrese un número positivo en las cifras significativas'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

		if x > - 1 and x < 1:
			respuesta = Lnx(cifras,x).lnx
			return Response(respuesta, status = status.HTTP_200_OK)
		else:
			resultado['error'] = 'El valor de x debe pertencer al intervalo ]-1;1['
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingresaste sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def sinhx(request):
	resultado = {}
	try:
		x = request.data['x']
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = "Ingrese un número positivo en las cifras significativas"
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

		respuesta = Sinhx(cifras, x).sinhx
		return Response(respuesta, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingresaste sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def arcsinx(request):
	resultado = {}
	try:
		x = float(request.data['x'])
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = "Ingrese un número positivo en las cifras significativas"
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

		if x > -1 and x  < 1:
			respuesta = Arcsinx(cifras,x).arcsinx
			return Response(respuesta, status = status.HTTP_200_OK)
		else:
			resultado['error'] = 'El valor de x debe pertencer al intervalo ]-1;1['
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingresaste sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

#=============== UNIDAD 2 ==================
@api_view(['POST'])
def biseccion(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = 'Ingresa un número positivo en las cifras significativas'
			return Response(resultado,status = status.HTTP_400_BAD_REQUEST)
		funcion = request.data['funcion']
		limites = request.data['params']
		respuesta = Biseccion(funcion,limites,cifras).biseccion
		if respuesta == False:
			resultado['error'] = 'El método no converge con los parámetros ingresados. Intenta con el método de Newton-Raphson!'
			return Response(resultado,status = status.HTTP_406_NOT_ACCEPTABLE)
		resultado = respuesta
		return Response(resultado, status = status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado,status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def falsaPosicion(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = 'Ingresa un número positivo en las cifras significativas'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		funcion = request.data['funcion']
		limites = request.data['params']
		respuesta = FalsaPosicion(funcion,limites,cifras).falsa_posicion
		if respuesta == False:
			resultado['error'] = 'El método no converge con los parámetros ingresados. Intenta con el método de Newton-Raphson!'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		resultado = respuesta
		return Response(resultado, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def puntoFijo(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = 'Ingresa un número positivo en las cifras significativas'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		funcion = request.data['funcion']
		limites = request.data['params']
		respuesta = PuntoFijo(funcion,limites,cifras).punto_fijo()
		if respuesta == False:
			resultado['error'] = 'El método no converge con los parámetros ingresados. Intenta con el método de Newton-Raphson!'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		resultado = respuesta
		return Response(resultado, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def newtonRaphson(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = "Ingresa un número positivo en las cifras significativas"
		funcion = request.data['funcion']
		limites = request.data['params']
		resultado = Newton_Raphson(funcion,limites,cifras).newton_raphson
		return Response(resultado, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = "Asegurate que todos los datos que ingreses sean válidos"
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def bairstow(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = "Ingrese un número positivo en las cifras significativas"
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		funcion = request.data['funcion']
		limites = request.data['params']
		resultado = Bairstow(funcion,limites,cifras).bairstow
		return Response(resultado, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = "Asegurate que todos los datos que ingreses sean válidos"
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def muller(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = "Ingrese un número positivo en las cifras significativas"
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		funcion = request.data['funcion']
		parametros = request.data['params']
		resultado = Muller(funcion,parametros,cifras).muller
		return Response(resultado, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = "Asegurate que todos los datos que ingreses sean válidos"
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def secante(request):
	resultado = {}
	try:
		funcion = request.data['funcion']
		cifras = int(request.data['cifras'])
		parametros = request.data['params']

		if cifras < 1:
			resultado['error'] = "Ingrese un número positivo en las cifras significativas"
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		respuesta = Secante(funcion, parametros, cifras).secante

		if respuesta == False:
			resultado['error'] = 'El método no converge con los parámetros ingresados. Intenta cambiar las cantidades o prueba con otro método'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(respuesta, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingresaste sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

		
#=============== UNIDAD 3 ==================

@api_view(['POST'])
def lagrange(request):
	resultado = {}
	try:
		polinomio = request.data['polinomio']
		valor = request.data['interpolar']
		x = request.data['xi']
		y = request.data['fi']

		if polinomio == '' and len(y) == 0:
			resultado['error'] = 'Debes proporcionar un polinomio o una lista de valores para f(x)'

		if polinomio:
			resultado = Lagrange(xi = x, evalu=valor, funct=polinomio).lagrange
		else:
			resultado = Lagrange(xi=x, evalu=valor, fi=y).lagrange

		return Response(resultado, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def diferencias_divididas(request):
	resultado = {}
	try:
		polinomio = request.data['polinomio']
		valor = request.data['interpolar']
		x = request.data['xi']
		y = request.data['fi']

		if polinomio == '' and len(y) == 0:
			resultado['error'] = 'Debes proporcionar un polinomio o una lista de valores para f(x)'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

		if polinomio != '':
			resultado = DiferenciasDivididas(xi=x, evalu=valor, funct=polinomio).diferencias_divididas
		else:
			resultado = DiferenciasDivididas(xi=x, evalu=valor, fi=y).diferencias_divididas

		return Response(resultado, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def interpolacion_newton(request):
	resultado = {}
	try:
		polinomio = request.data['polinomio']
		valor = request.data['interpolar']
		x = request.data['xi']
		y = request.data['fi']

		if polinomio == '' and len(y) == 0:
			resultado['error'] = 'Debes proporcionar un polinomio o una lista de valores para f(x)'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

		if polinomio != '':
			resultado = InterpolacionNewton(x=x, interpolar=valor, funct=polinomio).interpolacion_newton
		else:
			resultado = InterpolacionNewton(x=x, interpolar=valor, y=y).interpolacion_newton

		return Response(resultado, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def hermite(request):
	resultado = {}
	try:
		funcion = request.data['polinomio']
		interpolar = request.data['interpolar']
		x = request.data['xi']
		y = request.data['fi']
		dy = request.data['dy']
		respuesta = ''
		if funcion != '':
			respuesta = Hermite(x,interpolar,funct = funcion).hermite
		elif funcion == '' and len(x) != 0 and len(y) != 0 and len(dy) != 0:
			x = list(map(lambda valor: float(valor), x))
			y = list(map(lambda valor: float(valor), y))
			dy = list(map(lambda valor: float(valor), dy))
			respuesta = Hermite(x,interpolar, y = y, dy = dy).hermite
		else:
			resultado['error'] = 'Debes ingresar un polinomio o una tabla de datos para que podamos darte una respuesta'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

		return Response(respuesta, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)


#=============== UNIDAD 4 ==================
@api_view(['POST'])
def derivacion(request):
	resultado = {}
	try:
		funcion = request.data['funcion']
		metodo = int(request.data['metodo'])
		valor = request.data['valor']
		orden = int(request.data['orden'])
		modo = int(request.data['modo'])
		x = request.data['x']
		y = request.data['y']
		respuesta = ''

		if funcion != '':
			espaciado = float(request.data['espaciado'])
			if metodo == 1:
				# Hacia adelante
				respuesta = Diferenciacion(valor=valor,h=espaciado,orden=orden,modo=modo,funcion=funcion).hacia_adelante()
			elif metodo == 2:
				# Hacia atras
				respuesta = Diferenciacion(valor=valor,h=espaciado,orden=orden,modo=modo,funcion=funcion).hacia_atras()
			elif metodo == 3:
				# centrada
				respuesta = Diferenciacion(valor=valor,h=espaciado,orden=orden,modo=modo,funcion=funcion).centrada()
			elif metodo == 4:
				# tres puntos
				respuesta = Diferenciacion(valor=valor,h=espaciado,orden=orden,modo=modo,funcion=funcion).tres_puntos()
			else:
				#cinco puntos
				respuesta = Diferenciacion(valor=valor,h=espaciado,orden=orden,modo=modo,funcion=funcion).cinco_puntos()

		elif len(x) != 0 and len(y) != 0:
			x = list(map(lambda value: float(value), x))
			y = list(map(lambda value: float(value), y))

			if metodo == 1:
				# Hacia adelante
				print("Se utilizar diferencias hacia adelante metodo 1")
				respuesta = Diferenciacion(valor=valor,orden=orden,modo=modo,x=x,y=y).hacia_adelante()
			elif metodo == 2:
				# Hacia atras
				respuesta = Diferenciacion(valor=valor,orden=orden,modo=modo,x=x,y=y).hacia_atras()
			elif metodo == 3:
				# centrada
				respuesta = Diferenciacion(valor=valor,orden=orden,modo=modo,x=x,y=y).centrada()
			elif metodo == 4:
				# tres puntos
				respuesta = Diferenciacion(valor=valor,orden=orden,modo=modo,x=x,y=y).tres_puntos()
			else:
				#cinco puntos
				respuesta = Diferenciacion(valor=valor,orden=orden,modo=modo,x=x,y=y).cinco_puntos()
		else:
			resultado['error'] = 'Debes ingresar una función o una tabla de datos para poder darte una respuesta'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

		if respuesta == "666":
			resultado['error'] = 'Si ingresaste una función, es necesario que especifiques un valor para h'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		elif respuesta == "404":
			resultado['error'] = 'No encontramos una fórmula para el método que estas buscando'
			return Response(resultado, status=status.HTTP_404_NOT_FOUND)
		elif respuesta == False:
			resultado['error'] = 'Los datos ingresados no son suficiente para aproximar una respuesta'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(respuesta, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def richardson(request):
	resultado = {}
	try:
		funcion = request.data['funcion']
		metodo = int(request.data['metodo'])
		valor = request.data['valor']
		espaciado = float(request.data['espaciado'])
		orden = int(request.data['orden'])
		modo = int(request.data['modo'])
		nivel = int(request.data['nivel'])

		respuesta = Richardson(nivel=nivel, valor=valor, metodo=metodo,h=espaciado,orden=orden,modo=modo,funcion=funcion).richardson

		if respuesta == "666":
			resultado['error'] = 'Si ingresaste una función, es necesario que especifiques un valor para h'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		elif respuesta == "404":
			resultado['error'] = 'No encontramos una fórmula para el método que estas buscando'
			return Response(resultado, status=status.HTTP_404_NOT_FOUND)
		elif respuesta == False:
			resultado['error'] = 'Los datos ingresados no son suficiente para aproximar una respuesta'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(respuesta, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def integracion(request):
	resultado = {}
	try:
		funcion = request.data['funcion']
		metodo = int(request.data['metodo'])
		a = request.data['a']
		b = request.data['b']
		x = request.data['x']
		y = request.data['y']
		respuesta = ''
		if funcion != "":
			n = int(request.data['n'])
			if metodo == 1:
				respuesta = Integracion(a=a, b=b, funcion=funcion).trapecio_multiple(n)
			elif metodo == 2:
				respuesta = Integracion(a=a, b=b, funcion=funcion).simpson1_3(n)
			else:
				respuesta = Integracion(a=a, b=b, funcion=funcion).simpson3_8(n)

		elif len(x) > 0 and len(y) > 0:
			x = list(map(lambda value: float(value), x))
			y = list(map(lambda value: float(value), y))

			if metodo == 1:
				respuesta = Integracion(a=a, b=b, x=x, y=y).trapecio_multiple(1)
			elif metodo == 2:
				respuesta = Integracion(a=a, b=b, x=x, y=y).simpson1_3(1)
			else:
				respuesta = Integracion(a=a, b=b, x=x, y=y).simpson3_8(1)

		else:
			resultado['error'] = 'Se debe proporcionar una función o una tabla de datos para poder hacer nuestro trabajo'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)


		if respuesta == "N131ER":
			resultado['error'] = 'El número de intervalos debe ser par.'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		elif respuesta == "N132ER":
			resultado['error'] = 'Los puntos deben estar equidistantes'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		elif respuesta == "500":
			resultado['error'] = 'El número de intervalos debe ser múltiplo de 3'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(respuesta, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Algo salió mal! Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def rosemberg(request):
	try:
		funcion = request.data['funcion']
		metodo = int(request.data['metodo'])
		a = request.data['a']
		b = request.data['b']
		nivel = int(request.data['nivel'])

		respuesta = Rosemberg(a=a,b=b,funcion=funcion,metodo=metodo,nivel=nivel).rosemberg
		return Response(respuesta, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Algo salió mal! Asegurate que todos los datos que ingresaste sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

#=============== UNIDAD 5 ==================

@api_view(['POST'])
def euler(request):
	resultado = {}
	try:
		ecuacion = request.data['ecuation']

		xi = request.data['xi']
		yi = request.data['yi']

		valor = request.data['value']
		h = float(request.data['h']) if request.data['h'] else ""
		n = int(request.data['n']) if request.data['n'] else ""

		respuesta = Euler(ecuacion,xi,yi,valor,h = h, n = n).euler

		if respuesta == "666":
			resultado['error'] = "Debes proporcionar al menos un espaciado o un valor para n"
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(respuesta, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingresaste sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def taylor(request):
	resultado = {}
	try:
		ecuation = request.data['ecuation']
		xi = request.data['xi']
		yi = request.data['yi']
		value = request.data['value']
		h = 0 if request.data['h'] == '' else float(request.data['h'])
		n = 0 if request.data['n'] == '' else int(request.data['n'])
		grade = 2 if request.data['grade'] == '' else int(request.data['grade'])
		ndiffs = request.data['ndiffs']

		respuesta = Taylor(ecuation, xi, yi, value, grado = grade, h = h, n = n, derivadas = ndiffs).taylor

		if respuesta == "666":
			resultado['error']  = "Debes proporcionar al menos un espaciado o un valor para n"
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(respuesta, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = "Asegurate que todos los datos que ingresaste sean válidos"
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		

@api_view(['POST'])
def rungekutta(request):
	resultado = {}
	try:
		ecuation = request.data['ecuation']
		xi = request.data['xi']
		yi = request.data['yi']
		value = request.data['value']
		h = 0 if request.data['h'] == '' else float(request.data['h'])
		n = 0 if request.data['n'] == '' else float(request.data['n'])
		grade = 4 if request.data['grade'] == '' else int(request.data['grade'])

		if grade < 2 or grade > 4:
			resultado['error'] = 'El grado mínimo para aproximar por el método de RungeKutta es 2 y el máximo es 4'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

		respuesta = ''
		if grade == 2:
			respuesta = RungeKutta(ecuation, xi, yi, value, h = h, n = n).rungekutta2
		elif grade == 3:
			respuesta = RungeKutta(ecuation, xi, yi, value, h = h, n = n).rungekutta3
		else:
			respuesta = RungeKutta(ecuation, xi, yi, value, h = h, n = n).rungekutta4

		if respuesta == "666":
			resultado['error'] = "Debes proporcionar al menos un espaciado (h) o un número de puntos (n)"
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(respuesta, status = status.HTTP_200_OK)
	except Exception:
		resultado['error'] = "Asegurate que todos los datos que ingresaste sean válidos"
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def adaptativo(request):
	resultado = {}
	resultado['error'] = 'Este método aún no está en funcionamiento! Regrese más tarde :)'
	return Response(resultado, status=status.HTTP_404_NOT_FOUND)

