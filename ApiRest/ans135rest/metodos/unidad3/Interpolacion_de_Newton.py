from sympy import *
from functools import reduce

class InterpolacionNewton:
	def __init__(self, x, interpolar, funct="", y=[]):
		self.x = list(map(lambda z: float(z), x))
		self.interpolar = interpolar
		self.funct = funct
		self.y = list(map(lambda z: float(z), y))
		self.b = []

	def eval(self, valor):
		x = symbols('x')
		return self.funct.subs(x,float(valor))

	def calcular_diferencias(self, diferencias, expansion = 1):
		self.b.append(diferencias[0])

		nuevas_diferencias = []

		for n in range(1, len(diferencias)):
			diferencia = (diferencias[n] - diferencias[n-1])/(self.x[n+expansion] - self.x[n-1])
			nuevas_diferencias.append(diferencia)

		if len(nuevas_diferencias) >= 1:
			expansion += 1
			self.calcular_diferencias(nuevas_diferencias, expansion)

	@property
	def interpolacion_newton(self):
		if self.funct != "":
			self.funct = sympify(self.funct.replace("^","**"))
			for valor in self.x:
				self.y.append(self.eval(valor))

		self.b.append(self.y[0])
		diferencias = []

		for n in range(1, len(self.y)):
			diferencia = (self.y[n] - self.y[n-1])/(self.x[n] - self.x[n-1])
			diferencias.append(diferencia)

		self.calcular_diferencias(diferencias)

		factores = []
		factores.append(self.b[0])
		factor = 1

		x = symbols('x')
		for n in range(1, len(self.b)):
			factor = factor * (x - float(self.x[n-1]))
			factores.append(self.b[n] * factor)

		polinomio = reduce(lambda x,y: x + y, factores)
		interpolacion = polinomio.subs(x, self.interpolar)

		polinomio = str(polinomio.expand())
		polinomio = polinomio.replace("**","^")
		polinomio = polinomio.replace("*","")

		respuesta = {
			"Polinomio": [polinomio],
			"Interpolación": [str(interpolacion)]
		}

		return respuesta
