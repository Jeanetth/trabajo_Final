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
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			return Response(status = status.HTTP_400_BAD_REQUEST)
		x = float(request.data['x'])
		resultado = Sinx(cifras,x).sinx
		return Response(resultado, status=status.HTTP_200_OK)
	except Exception:
		return Response(status = status.HTTP_400_BAD_REQUEST)

#=============== UNIDAD 2 ==================
@api_view(['POST'])
def biseccion(request):
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			return Response(status = status.HTTP_400_BAD_REQUEST)
		funcion = request.data['funcion']
		limites = request.data['params']
		resultado = Biseccion(funcion,limites,cifras).biseccion
		return Response(resultado, status = status.HTTP_200_OK)
	except Exception:
		return Response(status = status.HTTP_400_BAD_REQUEST)

	