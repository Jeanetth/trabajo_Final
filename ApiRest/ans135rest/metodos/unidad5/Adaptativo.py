from sympy import *
from rungekutta import RungeKutta

class Adaptativo(RungeKutta):
	def __init__(self,f, x0,y0,xf,h = 0,n = 0, pasos = 4):
		RungeKutta.__init__(self,f,x0,y0,xf,h,n)
		self.pasos = pasos

	@property
	def adaptativo(self):
		x = []
		ykutta = []

		if self.pasos == 2:
			rkutta = self.rungekutta2
			if rkutta == "666":
				return "666"
			x = rkutta['x']
			ykutta = rkutta['yrungekutta']
		elif self.pasos == 3:
			rkutta = self.rungekutta3
			if rkutta == "666":
				return "666"
			x = rkutta['x']
			ykutta = rkutta['yrungekutta']
		else:
			rkutta = self.rungekutta4
			if rkutta == "666":
				return "666"
			x = rkutta['x']
			ykutta = rkutta['yrungekutta']

		x = list(map(lambda val: float(val),x))
		ykutta = list(map(lambda val: float(val), ykutta))

		valores = []

		for k in range(self.pasos):
			valores.append(ykutta[k])

		for i in range(self.pasos - 1, int(self.n)):
			if self.pasos == 4:
				predictor = ykutta[i] + ((self.h/24)*(55*(self.eval(x[i],ykutta[i])) - 59*(self.eval(x[i-1],ykutta[i-1])) + 37*(self.eval(x[i-2],ykutta[i-2])) - 9*(self.eval(x[i-3],ykutta[i-3]))))
				corrector = ykutta[i] + ((self.h/24)*(9*(self.eval(x[i+1],predictor)) + 19*(self.eval(x[i],ykutta[i])) - 5*(self.eval(x[i-1],ykutta[i-1])) + (self.eval(x[i-2],ykutta[i-2]))))
			elif self.pasos == 3:
				predictor = ykutta[i] + ((self.h/12)*(23*(self.eval(x[i],ykutta[i])) - 16*(self.eval(x[i-1],ykutta[i-1])) + 5*(self.eval(x[i-2],ykutta[i-2]))))
				corrector = ykutta[i] + ((self.h/12)*(5*(self.eval(x[i+1],predictor)) + 8*(self.eval(x[i],ykutta[i])) - (self.eval(x[i-1],ykutta[i-1]))))
			else:
				predictor = ykutta[i] + ((self.h/2)*(3*(self.eval(x[i],ykutta[i])) - (self.eval(x[i-1],ykutta[i-1]))))
				corrector = ykutta[i] + ((self.h/2)*((self.eval(x[i+1],predictor)) + (self.eval(x[i],ykutta[i]))))

			valores.append(corrector)
		
		resultado = {
			'x': list(map(lambda val: str(float(val)), x)),
			'yadaptativo': list(map(lambda val: str(float(val)), valores))
		}

		return resultado
