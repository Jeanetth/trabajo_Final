from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from sympy import *
from sympy.plotting.plot import plot

@api_view(['GET'])
def metodo_grafico(request, expr):
	# base code ...
