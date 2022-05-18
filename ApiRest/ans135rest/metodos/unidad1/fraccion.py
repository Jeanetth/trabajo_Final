 # Serie de taylor para fraccion 

 import math 

 class Fraccion: 
 	def __init__(self, cifras, x): 
 	"""docstring for ClassName"""
 		self.cifras = cifras
 		self.x = x 
 		self.aproximaciones = [] 
 		self.error = [] 

 		@property
 		def fraccion(self):
 			# Error de tolerancia 
 			Ess = 0.5*(10**(2-self.cifras)); 
 			Ea = 1000 
 			aprocimacionActual = self.x  
 			n = 0

		while(Ea > Ess):

			self.aproximaciones.append(aproximacionActual)

			aproximacionAnterior = aproximacionActual

			aproximacionActual +=  ((-1)**n)*self.x**(2*n+1)

			Ea = abs((aproximacionActual - aproximacionAnterior)/aproximacionActual) * 100

			self.errores.append(Ea)

			n += 1

		resultado = {
			'Aproximaciones': self.aproximaciones,
			'Errores': self.errores,
		}

		return resultado
