import math

def factorial(n):
	fact = 1

	for i in range(1, n):
		fact += fact * i

	return fact

class Sinx:

	def __init__(self, cifras, x):
		self.cifras = cifras
		self.x = x
		self.aproximaciones = []
		self.errores = []

	@property
	def sinx(self):
		#Error de tolerancia
		Ess = 0.5 * (10**(2 - self.cifras));

		Ea = 100

		aproximacionActual = self.x

		n = 1

		while(Ea > Ess):

			self.aproximaciones.append(aproximacionActual)

			aproximacionAnterior = aproximacionActual

			aproximacionActual += ((-1)**n) * (self.x**(2*n + 1))/factorial(2*n + 1) 

			Ea = abs((aproximacionActual - aproximacionAnterior)/aproximacionActual) * 100

			self.errores.append(Ea)

			n += 1

		resultado = {
			'Aproximaciones': self.aproximaciones,
			'Errores': self.errores,
		}

		return resultado



