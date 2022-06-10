import math

class Lnx:

	def __init__(self, cifras, x):
		self.cifras = cifras
		self.x = x
		self.aproximaciones = []
		self.errores = []

	@property
	def lnx (self):
		#Error de tolerancia
		Ess = 0.5 * (10**(2 - self.cifras)); 

		Ea = 100

		aproximacionActual = self.x 

		n = 2

		while(Ea > Ess):

			self.aproximaciones.append(aproximacionActual)

			aproximacionAnterior = aproximacionActual

			aproximacionActual += (((-1)**n-1)/(n))*self.x**n

			Ea = abs((aproximacionActual - aproximacionAnterior)/aproximacionActual) * 100

			self.errores.append(Ea)

			n += 1

		resultado = {
			'Aproximaciones': self.aproximaciones,
			'Errores': self.errores,
		}

		return resultado
		