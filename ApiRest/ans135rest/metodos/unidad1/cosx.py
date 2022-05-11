import math

class Cosx:
	def __init__(self, x, cifras):
		self.x = x
		self.cifras = cifras
		self.aproximaciones = []
		self.errores = []

	@property
	def cosx(self):
		# Error de tolerancia
		es=(0.5*(10**(2-self.cifras)))
		n=1
		aproximacionActual=1
		ea=1000
		while ea>es:
			aproximacionAnterior=aproximacionActual
			aproximacionActual+=math.pow(-1,n)*(math.pow(self.x,2*n)/math.factorial(2*n))
			self.aproximaciones.append(aproximacionActual)
			ea=abs((aproximacionActual-aproximacionAnterior)/aproximacionActual)*100
			self.errores.append(ea)
			n=n+1
		resultado = {
			'Aproximaciones': self.aproximaciones,
			'Errores': self.errores
		}
		return resultado
