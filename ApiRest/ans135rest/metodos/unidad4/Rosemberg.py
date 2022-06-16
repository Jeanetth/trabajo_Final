from .Integracion import Integracion
from sympy import *

class Rosemberg(Integracion):
	def __init__(self, a, b, funcion,nivel = 2,metodo = 1):
		"""
			1. Trapecio Compuesto
			2. Simpson 1/3
			3. Simpson 3/8
		"""

		Integracion.__init__(self, a, b, funcion)
		self.nivel = nivel
		self.metodo = metodo
		self.resultado = {}

	def calcular_error(self, Va):
		x = symbols('x')
		Vv = integrate(self.funcion, (x, self.a, self.b))
		self.resultado["Valor Verdadero"] = [float(Vv)]
		Error = abs((Vv - Va)/Vv)*100
		self.resultado['Error'] = [float(Error)]


	def calcular_diferencias(self, integrales, n = 2):
		# las integrales del nivel en que encuentre la iteracion
		# para la primera iteracion, se almacenan las difrenecias de nivel 2
		bloque=[]

		for i in range(len(integrales) - 1):
			I = (((4**(n - 1)) * integrales[i+1]) - integrales[i])/((4**(n - 1)) - 1)
			bloque.append(I)

		if len(bloque) == 1:
			self.resultado['Aproximación'] = bloque[0]
		else:
			n += 1
			self.calcular_diferencias(bloque, n)


	@property
	def rosemberg(self):
		integrales = []

		for i in range(self.nivel):
			if self.metodo == 1:
				integrales.append(float(((self.trapecio_multiple(2**i))['Aproximación'])[0]))
			elif self.metodo == 2:
				integrales.append(float(((self.simpson1_3(2**(i+1)))['Aproximación'])[0]))
			else:
				integrales.append(float(((self.simpson3_8(2**i))['Aproximación'])[0]))

		self.calcular_diferencias(integrales)

		self.calcular_error(self.resultado['Aproximación'])
		self.resultado['Aproximación'] = [self.resultado['Aproximación']]

		return self.resultado


