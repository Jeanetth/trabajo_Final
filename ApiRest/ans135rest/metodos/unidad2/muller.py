from sympy import *
import math

class Muller:
	def __init__(self, funct, parametros, cifras):
		self.funct = sympify(funct.replace("^","**"))
		self.Xo = float(parametros[0])
		self.X1 = float(parametros[1])
		self.X2 = float(parametros[2])
		self.cifras = cifras
		self.aproximaciones = []
		self.errores = []

	@property
	def muller(self):
		x = symbols('x')
		#Error de tolerancia
		Es = 0.5 * (10**(2 - self.cifras))
		Ea = 100

		while Ea > Es:

			X2_anterior = self.X2

			fo = self.funct.subs(x, self.Xo)
			f1 = self.funct.subs(x, self.X1)
			f2 = self.funct.subs(x, self.X2)

			ho = self.X1 - self.Xo
			h1 = self.X2 - self.X1

			amp0 = (f1 - fo)/ho
			amp1 = (f2 - f1)/h1

			a = (amp1 - amp0)/(h1 + ho)
			b = (a * h1) + amp1
			c = f2

			Discriminante = math.pow(b,2) - (4*a*c)

			if Discriminante > 0:

				D = math.sqrt(Discriminante)

				self.Xo = self.X1
				self.X1 = self.X2

				if abs(b + D) > abs(b - D):
					self.X2 = self.X2 + ((-2*c)/(b + D))
				else:
					self.X2 = self.X2 - ((-2*c)/(b + D))

				self.aproximaciones.append(str(self.X2))
			else:
				r1 = self.X2/2
				i1 = math.sqrt(abs(Discriminante))/2
				self.aproximaciones.append(str(complex(r1,i1)))
				resultado = {
					"Aproximaciones": self.aproximaciones,
					"Errores": self.errores
				}

				return resultado

			Ea = abs((self.X2 - X2_anterior)/self.X2) * 100
			self.errores.append(str(Ea))

		resultado = {
			"Aproximaciones": self.aproximaciones,
			"Errores": self.errores
		}

		return resultado

