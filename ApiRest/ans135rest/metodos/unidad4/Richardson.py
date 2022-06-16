from .Derivacion import Diferenciacion
from sympy import *


class Richardson(Diferenciacion):
	# Richardson utiliza los metodos de diferenciacion finita para aproximar a una mejor respuesta
	# los parametros son iguales a los de la diferenciacion finita agregando el nivel de aproximacion
	def __init__(self, nivel,valor,metodo = 1, h="", orden=1, modo=2, funcion = "", x = [], y =[]):

		Diferenciacion.__init__(self,valor, h, orden, modo, funcion, x, y)

		self.nivel = nivel
		self.metodo = metodo
		self.resultado = {}

	def calcular_diferencias(self, diferencias, nivel = 2):
		# las diferencias del nivel en que se encuentre la iteracion
		# para la primera iteracion, se almacenan las diferencias de nivel 2
		bloque = []

		for i in range(len(diferencias) - 1):
			D = (((4**(nivel - 1)) * diferencias[i + 1]) - diferencias[i])/((4**(nivel - 1)) - 1)
			bloque.append(float(D))

		if len(bloque) == 1:
			self.resultado['Aproximación'] = [str(bloque[0])]
			return True
		else:
			nivel += 1
			self.calcular_diferencias(bloque, nivel)

	@property
	def richardson(self):
		self.validar()
		n = self.nivel
		intervalos = [self.h]

		for i in range(1,n):
			intervalos.append(intervalos[i-1]/2)

		diferencias = []

		for diferencia in intervalos:
			if self.metodo == 1:
				#diferencias hacia adelante
				aproximacion = self.hacia_adelante(diferencia)
				#print(type((aproximacion['Aproximación'])[0]))
				if aproximacion == "666":
					return "666"
				elif aproximacion == "404":
					return "404"
				elif aproximacion == False:
					return False
				else:
					diferencias.append((aproximacion['Aproximación'])[0])

			elif self.metodo == 2:
				#diferencias hacia atras
				aproximacion = self.hacia_atras(diferencia)
				#print(aproximacion['Aproximación'])
				if aproximacion == "666":
					return "666"
				elif aproximacion == "404":
					return "404"
				elif aproximacion == False:
					return False
				else:
					diferencias.append((aproximacion['Aproximación'])[0])
			elif self.metodo == 3:
				#diferencias centradas
				aproximacion = self.centrada(diferencia)
				#print(aproximacion['Aproximación'])
				if aproximacion == "666":
					return "666"
				elif aproximacion == "404":
					return "404"
				elif aproximacion == False:
					return False
				else:
					diferencias.append((aproximacion['Aproximación'])[0])
			elif self.metodo == 4:
				# metodo de los tres puntos
				aproximacion = self.tres_puntos(diferencia)
				#print(aproximacion['Aproximación'])
				if aproximacion == "666":
					return "666"
				elif aproximacion == "404":
					return "404"
				elif aproximacion == False:
					return False
				else:
					diferencias.append((aproximacion['Aproximación'])[0])
			elif self.metodo == 5:
				#metodo de los cinco puntos
				aproximacion = self.cinco_puntos(diferencia)
				#print(aproximacion['Aproximación'])
				if aproximacion == "666":
					return "666"
				elif aproximacion == "404":
					return "404"
				elif aproximacion == False:
					return False
				else:
					diferencias.append((aproximacion['Aproximación'])[0])

		self.calcular_diferencias(diferencias)

		x = symbols('x')
		derivada = diff(self.funcion, x, self.orden)
		Vv = derivada.subs(x, float(self.valor))
		self.resultado['Valor Verdadero'] = [str(Vv)]
		Error = abs((float(Vv) - float((self.resultado['Aproximación'])[0]))/float(Vv)) * 100
		self.resultado['Error'] = [str(Error)]

		return self.resultado

