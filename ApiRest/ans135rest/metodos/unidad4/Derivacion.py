from sympy import *
import math

class Diferenciacion:
	def __init__(self,valor, h="", orden=1, modo=2, funcion = "", x = [], y =[]):
		"""
			- valor: valor flotante en el que se desea aproximar la derivada

			- h: valor flotante que indica el tamaño del espaciado. Si se ingresa una funcion
				es necesario especificar el valor para h, pero si se proporciona una tabla con valores
				para x y y, el valor de h se calculara automaticamente.

			- orden: valor entero positivo entre 1 y 4 que indica el orden de la derivada, donde:
				1 = primer derivada
				2 = segunda derivada
				3 = tercer derivada
				4 = cuarta derivada
				(Por defecto calcula la primer derivada)

			- modo: valor entero positivo, dos opciones 1 y 2 donde:
				1 = primer modo para calcular la Aproximación a la derivada
				2 = segundo modo para calcular la Aproximación a la derivada, normalmente es mas preciso que el primero
				(Por defecto se realiza la Aproximación con el segundo modo para mayor precision)

			- funcion: texto, hace referencia a una funcion geometrica, polinomio, exponencial, etc.
				Este parametro es opcional, de no ser necesario ingresar una funcion, se puede proporcionar como alternativa
				una tabla de puntos que corresponden a valores de x y valores de y

			- x: Lista de valores en formato flotante que corresponde a los valores de x. Una alternativa si no ingresamos una funcion

			- y: Lista de valores en formato flotante que corresponde a los valores de y. Parametro obligatorio si ya se ingreso una lista
				de puntos para valores de x anteriormente.
		"""

		self.valor = sympify(valor)
		self.h = h
		self.orden = orden
		self.modo = modo
		self.funcion = sympify(funcion.replace("^","**")) if funcion else ""
		self.x = x
		self.y = y
		self.resultado = {}

	def __evaluar(self, punto):
		# devuelve el valor de la funcion evaluada en el punto pasado por parametro
		x = symbols('x')
		return self.funcion.subs(x, float(punto))

	def validar(self):
		if self.funcion != "" and self.h == "":
			return "666"

		if len(self.x) > 0 and len(self.y) > 0 and self.h == "":
			# se calcula el valor de h en base a los valores de x ingresados
			self.h = abs(self.x[1] - self.x[0])

	def calcular_error(self, Va):
		x = symbols('x')
		if self.funcion != "":
			derivada  = diff(self.funcion, x, self.orden)
			Vv = derivada.subs(x, self.valor)
			Vv = float(Vv)
			self.resultado['Valor Verdadero'] = [str(Vv)]
			Error = abs((Vv - Va)/Vv)*100
			Error = float(Error)
			self.resultado['Error'] = [str(Error)]


	# *********************** DIFERENCIAS FINITAS HACIA ADELANTE *******************
	def hacia_adelante(self, espaciado = ""):
		self.validar()

		if espaciado != "":
			self.h = espaciado
		# ========== FORMULAR DE Aproximación PARA PRIMERA, SEGUNDA, TERCERA Y CUARTA DERIVADA HACIA ADELANTE CON EL MODO 1 =========
		if self.modo == 1:
			# =============== PRIMER DERIVADA HACIA ADELANTE (MODO 1) ===============
			if self.orden == 1:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				# devuelve el indice del valor a aproximar dentro de la lista
				h = self.x.index(self.valor)

				try:
					dx = (self.y[h + 1] - self.y[h])/(self.h)
				except Exception:
					return False

				self.resultado['Aproximación'] = float(dx)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== SEGUNDA DERIVADA HACIA ADELANTE (MODO 1) ===============
			elif self.orden == 2:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					self.x.append(self.valor + (2*self.h))
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d2x = (self.y[h + 2] - (2*self.y[h + 1]) + self.y[h])/(math.pow(self.h,2))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d2x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== TERCERA DERIVADA HACIA ADELANTE (MODO 1) ===============
			elif self.orden == 3:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (3*self.h))
					self.x.append(self.valor - (2*self.h))
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d3x = (self.y[h] - (3*self.y[h - 1]) + (3*self.y[h - 2]) - self.y[h - 3])/(math.pow(self.h, 3))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d3x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== CUARTA DERIVADA HACIA ADELANTE (MODO 1) ===============
			elif self.orden == 4:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (4*self.h))
					self.x.append(self.valor - (3*self.h))
					self.x.append(self.valor - (2*self.h))
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d4x = (self.y[h] - (4*self.y[h - 1]) + (6*self.y[h - 2]) - (4*self.y[h - 3]) + self.y[h - 4])/(math.pow(self.h, 4))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d4x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

		# ========== FORMULAR DE Aproximación PARA PRIMERA, SEGUNDA, TERCERA Y CUARTA DERIVADA HACIA ADELANTE CON EL MODO 1 =========
		elif self.modo == 2:

			# =============== PRIMER DERIVADA HACIA ADELANTE (MODO 2) ===============
			if self.orden == 1:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					self.x.append(self.valor + (2*self.h))
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					dx = (-self.y[h + 2] + (4*self.y[h + 1]) - (3*self.y[h]))/(2*self.h)
				except Exception:
					return False

				self.resultado['Aproximación'] = float(dx)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== SEGUNDA DERIVADA HACIA ADELANTE (MODO 2) ===============
			if self.orden == 2:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					self.x.append(self.valor + (2*self.h))
					self.x.append(self.valor + (3*self.h))
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d2x = (-self.y[h + 3] + (4*self.y[h + 2]) - (5*self.y[h + 1]) + (2*self.y[h]))/(math.pow(self.h,2))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d2x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== TERCER DERIVADA HACIA ADELANTE (MODO 2) ===============
			if self.orden == 3:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					self.x.append(self.valor + (2*self.h))
					self.x.append(self.valor + (3*self.h))
					self.x.append(self.valor + (4*self.h))	
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d3x = (-(3*self.y[h + 4]) + (14*self.y[h + 3]) - (24*self.y[h + 2]) + (18*self.y[h + 1]) - self.y[h])/(2*(math.pow(self.h,3)))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d3x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== CUARTA DERIVADA HACIA ADELANTE (MODO 2) ===============
			if self.orden == 4:
				if self.funcion != "":
					self.x = []
					self.y = []	
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					self.x.append(self.valor + (2*self.h))
					self.x.append(self.valor + (3*self.h))
					self.x.append(self.valor + (4*self.h))
					self.x.append(self.valor + (5*self.h))
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d4x = (-(2*self.y[h + 5]) + (11*self.y[h + 4]) - (24*self.y[h + 3]) + (26*self.y[h + 1]) + (3*self.y[h]))/(math.pow(self.h,4))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d4x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

	# *********************** DIFERENCIAS FINITAS HACIA ATRAS *******************
	def hacia_atras(self, espaciado = ""):
		self.validar()

		if espaciado != "":
			self.h = espaciado

		# ========== FORMULAR DE Aproximación PARA PRIMERA, SEGUNDA, TERCERA Y CUARTA DERIVADA HACIA ATRAS CON EL MODO 1 =========
		if self.modo == 1:
			# =============== PRIMER DERIVADA HACIA ATRAS (MODO 1) ===============
			if self.orden == 1:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				# devuelve el indice del valor a aproximar dentro de la lista
				h = self.x.index(self.valor)

				try:
					dx = (self.y[h] - self.y[h - 1])/(self.h)
				except Exception:
					return False

				self.resultado['Aproximación'] = float(dx)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== SEGUNDA DERIVADA HACIA ATRAS (MODO 1) ===============
			elif self.orden == 2:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (2*self.h))
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d2x = (self.y[h] - (2*self.y[h - 1]) + self.y[h - 2])/(math.pow(self.h,2))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d2x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== TERCERA DERIVADA HACIA ATRAS (MODO 1) ===============
			elif self.orden == 3:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (3*self.h))
					self.x.append(self.valor - (2*self.h))
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d3x = (self.y[h] - (3*self.y[h - 1]) + (3*self.y[h - 2]) - self.y[h - 3])/(math.pow(self.h, 3))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d3x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== CUARTA DERIVADA HACIA ATRAS (MODO 1) ===============
			elif self.orden == 4:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (4*self.h))
					self.x.append(self.valor - (3*self.h))
					self.x.append(self.valor - (2*self.h))
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d4x = (self.y[h] - (4*self.y[h - 1]) + (6*self.y[h - 2]) - (4*self.y[h - 3]) + self.y[h - 4])/(math.pow(self.h, 4))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d4x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

		# ========== FORMULAR DE Aproximación PARA PRIMERA, SEGUNDA, TERCERA Y CUARTA DERIVADA CON EL MODO 1 =========
		elif self.modo == 2:

			# =============== PRIMER DERIVADA HACIA ATRAS (MODO 2) ===============
			if self.orden == 1:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (2*self.h))
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					dx = ((3*self.y[h]) - (4*self.y[h - 1]) + self.y[h - 2])/(2*self.h)
				except Exception:
					return False

				self.resultado['Aproximación'] = float(dx)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== SEGUNDA DERIVADA HACIA ATRAS (MODO 2) ===============
			if self.orden == 2:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (3*self.h))
					self.x.append(self.valor - (2*self.h))
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d2x = ((2*self.y[h]) - (5*self.y[h - 1]) + (4*self.y[h - 2]) - self.y[h - 3])/(math.pow(self.h,2))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d2x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== TERCER DERIVADA HACIA ATRAS (MODO 2) ===============
			if self.orden == 3:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (4*self.h))
					self.x.append(self.valor - (3*self.h))
					self.x.append(self.valor - (2*self.h))
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)	
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d3x = ((5*self.y[h]) - (18*self.y[h - 1]) + (24*self.y[h - 2]) - (14*self.y[h - 3]) + (3*self.y[h - 4]))/(math.pow(self.h,3))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d3x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== CUARTA DERIVADA HACIA ADELANTE (MODO 2) ===============
			if self.orden == 4:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (5*self.h))
					self.x.append(self.valor - (4*self.h))
					self.x.append(self.valor - (3*self.h))
					self.x.append(self.valor - (2*self.h))	
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d4x = ((3*self.y[h]) - (14*self.y[h - 1]) + (26*self.y[h - 2]) - (24*self.y[h - 3]) + (11*self.y[h - 4]) - (2*self.y[h - 5]))/(math.pow(self.h,4))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d4x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado


	# *********************** DIFERENCIAS FINITAS CENTRADAS *******************
	def centrada(self, espaciado = ""):
		self.validar()

		if espaciado != "":
			self.h = espaciado

		# ========== FORMULAS DE Aproximación PARA PRIMERA, SEGUNDA, TERCERA Y CUARTA DERIVADA CENTRADA CON EL MODO 1 =========
		if self.modo == 1:
			# =============== PRIMER DERIVADA CENTRADA (MODO 1) ===============
			if self.orden == 1:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				# devuelve el indice del valor a aproximar dentro de la lista
				h = self.x.index(self.valor)

				try:
					dx = (self.y[h + 1] - self.y[h - 1])/(2*self.h)
				except Exception:
					return False

				self.resultado['Aproximación'] = float(dx)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== SEGUNDA DERIVADA CENTRADA (MODO 1) ===============
			elif self.orden == 2:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d2x = (self.y[h + 1] - (2*self.y[h]) + self.y[h - 1])/(math.pow(self.h,2))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d2x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== TERCERA DERIVADA CENTRADA (MODO 1) ===============
			elif self.orden == 3:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (2*self.h))
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					self.x.append(self.valor + (2*self.h))
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d3x = (self.y[h + 2] - (2*self.y[h + 1]) + (2*self.y[h - 1]) - self.y[h - 2])/(2*(math.pow(self.h, 3)))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d3x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== CUARTA DERIVADA CENTRADA (MODO 1) ===============
			elif self.orden == 4:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (2*self.h))
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					self.x.append(self.valor + (2*self.h))
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d4x = (self.y[h + 2] - (4*self.y[h + 1]) + (6*self.y[h]) - (4*self.y[h - 1]) + self.y[h - 2])/(math.pow(self.h, 4))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d4x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

		# ========== FORMULAR DE Aproximación PARA PRIMERA, SEGUNDA, TERCERA Y CUARTA DERIVADA CENTRADA CON EL MODO 2 =========
		elif self.modo == 2:

			# =============== PRIMER DERIVADA CENTRADA (MODO 2) ===============
			if self.orden == 1:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (2*self.h))
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					self.x.append(self.valor + (2*self.h))
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					dx = (-self.y[h + 2] + (8*self.y[h + 1]) - (8*self.y[h - 1]) + self.y[h - 2])/(12*self.h)
				except Exception:
					return False

				self.resultado['Aproximación'] = float(dx)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== SEGUNDA DERIVADA CENTRADA (MODO 2) ===============
			if self.orden == 2:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (2*self.h))
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					self.x.append(self.valor + (2*self.h))
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d2x = (-self.y[h + 2] + (16*self.y[h + 1]) - (30*self.y[h]) + (16*self.y[h - 1]) - self.y[h - 2])/(12*(math.pow(self.h,2)))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d2x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== TERCER DERIVADA CENTRADA (MODO 2) ===============
			if self.orden == 3:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (3*self.h))
					self.x.append(self.valor - (2*self.h))
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					self.x.append(self.valor + (2*self.h))
					self.x.append(self.valor + (3*self.h))
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d3x = (-self.y[h + 3] + (8*self.y[h + 2]) - (12*self.y[h + 1]) + (12*self.y[h - 1]) - (8*self.y[h - 2]) + self.y[h - 3])/(8*(math.pow(self.h,3)))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d3x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# =============== CUARTA DERIVADA CENTRADA (MODO 2) ===============
			if self.orden == 4:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (3*self.h))
					self.x.append(self.valor - (2*self.h))
					self.x.append(self.valor - self.h)	
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					self.x.append(self.valor + (2*self.h))
					self.x.append(self.valor + (3*self.h))
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d4x = (-self.y[h + 3] + (12*self.y[h + 2]) - (34*self.y[h + 1]) + (56*self.y[h]) - (39*self.y[h - 1]) + (12*self.y[h - 2]) - self.y[h - 3])/(6*(math.pow(self.h,4)))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d4x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado


	# =============== DIFERENCIAS FINITAS POR EL METODO DE LOS TRES PUNTOS =================
	def tres_puntos(self, espaciado = ""):
		self.validar()

		if espaciado != "":
			self.h = espaciado

		if self.modo == 1:
			# ====== PRIMER DERIVADA POR EL METODO DE LOS TRES PUNTOS =======
			if self.orden == 1:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					dx = (self.y[h + 1] - self.y[h - 1])/(2*self.h)
				except Exception:
					return False

				self.resultado['Aproximación'] = float(dx)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado

			# ======= SEGUNDA DERIVADA POR EL METODOS DE LOS TRES PUNTOS ====== 
			elif self.orden == 2:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					d2x = (self.y[h + 1] - (2*self.y[h]) + self.y[h - 1])/(math.pow(self.h,2))
				except Exception:
					return False

				self.resultado['Aproximación'] = float(d2x)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado
			elif self.orden > 2:
				return "404"

		elif self.modo == 2:
			if self.orden == 1:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					self.x.append(self.valor + (2*self.h))
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					dx = (-(3*self.y[h]) + (4*self.y[h + 1]) - self.y[h + 2])/(2*self.h)
				except Exception:
					return False

				self.resultado['Aproximación'] = float(dx)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado
			elif self.orden > 1:
				return "404"

	# =============== DIFERENCIAS FINITAS POR EL METODO DE LOS CINCO PUNTOS =================
	def cinco_puntos(self, espaciado=""):
		self.validar()

		if espaciado != "":
			self.h = espaciado

		if self.modo == 1:
			if self.orden == 1:
				if self.funcion != "":
					self.x = []
					self.y = []
					self.x.append(self.valor - (2*self.h))
					self.x.append(self.valor - self.h)
					self.x.append(self.valor)
					self.x.append(self.valor + self.h)
					self.x.append(self.valor + (2*self.h))
					for punto in self.x:
						self.y.append(self.__evaluar(punto))

				h = self.x.index(self.valor)

				try:
					dx = (1/(12*self.h)) * (self.y[h - 2] - (8*self.y[h - 1]) + (8*self.y[h + 1]) - self.y[h + 2])
				except Exception:
					return False

				self.resultado['Aproximación'] = float(dx)
				self.calcular_error(self.resultado['Aproximación'])
				self.resultado['Aproximación'] = [self.resultado['Aproximación']]
				return self.resultado
			elif self.orden > 1:
				return "404"
		elif self.modo > 1:
			return "404"











		
