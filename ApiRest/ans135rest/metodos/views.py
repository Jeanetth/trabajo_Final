from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
# =========== UNIDAD 1 ==========
from metodos.unidad1.sinx import Sinx
from metodos.unidad1.cosx import Cosx
from metodos.unidad1.coshx import Coshx
# =========== UNIDAD 2 ==========
from metodos.unidad2.biseccion import Biseccion
from metodos.unidad2.falsa_posicion import FalsaPosicion
from metodos.unidad2.punto_fijo import PuntoFijo
from metodos.unidad2.newton_raphson import Newton_Raphson
from metodos.unidad2.bairstow import Bairstow

#=============== UNIDAD 1 ==================

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
		print(resultado)
		print(type(resultado))
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
			resultado['error'] = "Ingrese un número positivo en las cifras significativas"
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
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

#=============== UNIDAD 3 ==================
















	