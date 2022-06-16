from sympy import *

class Integracion:
	def __init__(self, a, b, funcion="", x = [], y = []):
		"""
			a - (float) limite inferior de la integral
			b - (float) limite superior de la integral
			n - (int) numero de subintervalos entre a y b. Mientras mayor sea el numero de subintervalos
				mayor sera la aproximacion al area bajo la curva. En caso de ingresar una tabla de datos, se calculara
				de forma automatica y puede omitirse. Por defecto el valor es 1 utilizando unicamente
				el intervalo inferior y el intervalo superior para aproximarse a la respuesta.
				No se recomienda si se requiere mucha precision
				precision.
			funcion - (string) funcion polinomial o geometrica. Este parametro es opcional ya que como
				alternativa puede proporcionarse una tabla de valores, si ese es el caso, puede omitirse
				el ingreso de una funcion pero no ambas.
			x - (list(float)) corresponde a una serie de puntos del eje x en los que se evalua la funcion.
				Este parametro es util cuando se tiene una tabla de datos xy, como complemento obligatorio
				se debe proporcionar una lista de valores para y que deben ser la imagen de cada valor de x
				respectivo.
			y - (list(float)) corresponde al valor de una funcion evaluada en un punto x en especifico.
				este parametro es obligatorio si ya se ingreso anteriormente una lista de puntos para valores
				de x.

		"""
		self.a = sympify(a)
		self.b = sympify(b)
		#sub = n # numero de intervalos
		self.funcion = sympify(funcion.replace("^","**")) if funcion != "" else ""
		self.x = x
		self.y = y
		self.h = 0
		self.respuesta = {}

	def evaluar(self, valor):
		x, y, z = symbols('x y z')
		if 'x' in str(self.funcion):
			return self.funcion.subs(x, float(valor))
		elif 'y' in str(self.funcion):
			return self.funcion.subs(y, float(valor))
		elif 'z' in str(self.funcion):
			return self.funcion.subs(z, float(valor))

	def validar(self, sub):
		if self.funcion != "":
			self.x = []
			self.y = []
			#tamano del espaciado
			self.h = (float(self.b) - float(self.a))/sub

			self.x.append(float(self.a))

			for i in range(1,sub):
				self.x.append(float(self.x[i-1] + self.h))

			self.x.append(float(self.b))

			for valor in self.x:
				self.y.append(float(self.evaluar(valor)))

		elif self.funcion == "" and len(self.x) > 0 and len(self.y) > 0:
			# tamano del espaciado para una tabla de datos
			igual_espaciado = True
			h_inicial = float(self.x[1]) - float(self.x[0])

			for i in range(2, len(self.x)):
				h_actual = float(self.x[i]) - float(self.x[i-1])
				if h_actual != h_inicial:
					igual_espaciado = False
					break

			if igual_espaciado:
				self.h = h_inicial
			else:
				self.h = []
				for i in range(1,len(self.x)):
					self.h.append(float(self.x[i]) - float(self.x[i-1]))
		else:
			return "666"

	def calcular_error(self, Va):
		if self.funcion != "":
			x = symbols('x')
			Vv = integrate(self.funcion, (x,self.a,self.b))
			self.respuesta['Valor Verdadero'] = [float(Vv)]
			Error = abs((Vv - Va)/Vv) * 100
			self.respuesta['Error'] = [float(Error)]

	def trapecio_multiple(self, sub):
		
		self.validar(sub)

		respuesta = 0

		if type(self.h) == float:				
			for k in range(len(self.x) - 1):
				respuesta += (self.h) * ((self.y[k] + self.y[k+1])/2)
		else:
			for k in range(len(self.x) - 1):
				respuesta += (float(self.h[k]) * ((float(self.y[k]) + float(self.y[k+1]))/2))

		try:
			self.respuesta['Aproximación'] = float(respuesta)
			self.calcular_error(self.respuesta['Aproximación'])
			self.respuesta['Aproximación'] = [self.respuesta['Aproximación']]
			return self.respuesta
		except TypeError:
			self.respuesta['Aproximación'] = [str(respuesta.expand()).replace("**","^")]
			return self.respuesta


	def simpson1_3(self, sub):
		self.validar(sub)

		if len(self.x)%2 == 0:
			return "N131ER"
		if type(self.h) != float:
			return "N132ER"

		suma_i = 0
		for i in range(1, len(self.y) - 1, 2):
			suma_i += self.y[i]

		suma_j = 0
		for j in range(2, len(self.y) - 2, 2):
			suma_j += self.y[j]


		respuesta = (self.h) * ((self.y[0] + (4*suma_i) + (2*suma_j) + self.y[-1])/3)

		try:
			self.respuesta['Aproximación'] = float(respuesta)
			self.calcular_error(self.respuesta['Aproximación'])
			self.respuesta['Aproximación'] = [self.respuesta['Aproximación']]
			return self.respuesta
		except TypeError:
			self.respuesta['Aproximación'] = [str(respuesta.expand()).replace("**","^")]
			return self.respuesta

	def simpson3_8(self,sub):
		self.validar(sub)

		if (len(self.x)-1)%3 == 0 and self.funcion == "" and type(self.h) == float:
			respuesta = 0
			for i in range(3, len(self.x), 3):
				respuesta += (self.h) * ((self.y[i-3] + 3*self.y[i-2] + 3*self.y[i-1] + self.y[i])/8)

			try:
				return float(respuesta)
			except TypeError:
				return str(respuesta.expand()).replace("**","^")

		elif type(self.h) == float and self.funcion != "":
			respuesta = 0
			for i in range(len(self.x) - 1):
				sub = [self.y[i]]
				for j in range(3):
					sub.append(self.evaluar(self.x[i] + ((self.h/3) * (j+1))))
				sub.append(self.y[i + 1])

				respuesta += (self.h) * ((sub[0] + 3*sub[1] + 3*sub[2] + sub[3])/8)

			try:
				self.respuesta['Aproximación'] = float(respuesta)
				self.calcular_error(self.respuesta['Aproximación'])
				self.respuesta['Aproximación'] = [self.respuesta['Aproximación']]
				return self.respuesta
			except TypeError:
				self.respuesta['Aproximación'] = [str(respuesta.expand()).replace("**","^")]
				return self.respuesta
		else:
			return "500"
