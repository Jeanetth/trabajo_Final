from sympy import *
import math
import re
import numpy as np

x,r,s = symbols('x,r,s')

class Bairstow:

	def __init__(self,expr,params, signif):
		self.expr = expr
		self.r = float(params[0])
		self.s = float(params[1])
		self.signif = signif
		self.roots = []

	def _flatten(self,pol):
		pol = pol.replace(' ','')
		pol = pol.replace('^','**')
		pattern_coeff = r'((-?\d*[.]?\d*)\*?x{1}\**(\d*))'
		pattern_indterm = r'(-?\d*[.{1}]?\d*$)'
		result = re.findall(pattern_coeff, pol)
		max_grade = int((result[0])[-1]) if (result[0])[-1] != '' else 1
		independent_term = re.search(pattern_indterm, pol).group()
		coefficients = []	
		for pos in range(len(result)):
			grade = int((result[pos])[-1]) if (result[pos])[-1] else 1
			if grade != max_grade:
				add_term = 'x**{}'.format(max_grade)
				result.insert(pos,(add_term,'0',max_grade))
				pos-=1
			max_grade -= 1

		min_grade = int((result[-1])[-1]) if (result[-1])[-1] else 1

		if min_grade > 1:
			for i in range(min_grade-1, 0, -1):
				result.append(('0*x**{}'.format(i),'0',str(i)))
		elif (result[-1])[-1] == '':
			grade_one = result.pop()
			result.append((grade_one[0],grade_one[1],1))

		for _,num,_ in result:
			if num == '-':
				coefficients.append(-1.0)
			elif num == '':
				coefficients.append(1.0)
			else:
				coefficients.append(float(num))

		coefficients.append(float(independent_term)) if independent_term != '' else coefficients.append(0.0)
		return coefficients

	def _gauss_jordan(self,b, c):
		matrix = np.zeros((2,3))

		matrix[0][0] = c[-2]
		matrix[0][1] = c[-3]
		matrix[0][2] = -b[-2]
		matrix[1][0] = c[-1]
		matrix[1][1] = c[-2]
		matrix[1][2] = -b[-1]

		deltas = []

		for i in range(2):
			if matrix[i][i] == 0:
				raise Exception
			for j in range(2):
				if i != j:
					ratio = matrix[j][i]/matrix[i][i]
					for k in range(3):
						matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

		for i in range(2):
			deltas.append(matrix[i][2]/matrix[i][i])

		return deltas

	def _Quadroot(self):
		disc = math.pow(self.r,2) + (4*self.s)

		if disc > 0:
			x1 = (self.r + math.sqrt(disc))/2
			x2 = (self.r - math.sqrt(disc))/2
			self.roots.append(str(x1))
			self.roots.append(str(x2))
		else:
			x1 = self.r/2
			x2 = x1
			i1 = math.sqrt(abs(disc))/2
			i2 = -i1
			r1 = complex(x1,i1)
			r2 = complex(x2,i2)
			self.roots.append(str(r1))
			self.roots.append(str(r2))
		return self.roots

	def _Quadratic(self):
		coefficients = self._flatten(self.expr)
		a = coefficients[0]
		b = coefficients[1]
		c = coefficients[2]

		disc = math.pow(b,2) - (4*a*c)

		if disc > 0:
			x1 = (-b + math.sqrt(disc))/(2*a)
			x2 = (-b - math.sqrt(disc))/(2*a)
			self.roots.append(str(x1))
			self.roots.append(str(x2))
		else:
			x1 = b/2
			x2 = x1
			i1 = math.sqrt(abs(disc))/(2*a)
			i2 = -i1
			r1 = complex(x1,i1)
			r2 = complex(x2,i2)
			self.roots.append(str(r1))
			self.roots.append(str(r2))
		return self.roots

	@property
	def bairstow(self):
		coefficients = self._flatten(self.expr)
		Es = 0.5 * math.pow(10, 2-self.signif)
		Ear = 100
		Eas = 100
		while Ear > Es and Eas > Es:
			# valores para b
			b = []
			b.append(coefficients[0])
			b.append(coefficients[1] + (self.r*b[0])) 
			for i in range(2, len(coefficients)):
				b.append(coefficients[i] + (self.r*b[i-1]) + (self.s*b[i-2]))

			# valores para c
			c = []
			c.append(b[0])
			c.append(b[1] + (self.r*b[0]))
			for i in range(2, len(b) - 1):
				c.append(b[i] + (self.r*c[i-1]) + (self.s*c[i-2]))

			deltas = self._gauss_jordan(b, c)

			self.r = self.r + deltas[0]
			self.s = self.s + deltas[1]

			Ear = abs(deltas[0]/self.r) * 100
			Eas = abs(deltas[1]/self.s) * 100

		# se calcula el cociente
		dividend = sympify(self.expr)	
		divider = sympify("x**2-r*x-s") 
		divider = divider.subs([(r,float(self.r)), (s,float(self.s))])
		quotient, _ = div(dividend, divider, domain='RR')
		quotient = str(quotient)

		new_coefficients = self._flatten(quotient)

		grade = len(new_coefficients) - 1

		self._Quadroot()
		self.expr = quotient
		if grade >= 3:
			self.bairstow
		elif grade == 2:
			self._Quadratic()
		else:
			x = self._flatten(quotient)
			x = -x[-1]
			self.roots.append(str(x))

		resultado = {
			'Raices': self.roots,
		}
		return resultado
