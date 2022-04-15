from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from sympy import *
from sympy.plotting.plot import plot
from metodos.unidad1.sinx import Sinx
from metodos.unidad2.biseccion import Biseccion 

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

	