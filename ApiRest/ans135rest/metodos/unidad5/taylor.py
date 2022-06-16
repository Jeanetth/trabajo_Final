from sympy import *
import numpy as np
from math import pow, factorial

class Taylor:
    def __init__(self, funct, xi, yi, xf, grado = 2, h = 0, n = 0, derivadas = []):
        self.funct = sympify(funct.replace("^","**"))
        self.xi = sympify(xi)
        self.yi = sympify(yi)
        self.xf = sympify(xf)
        self.grado = grado
        self.h = h
        self.n = n
        self.derivadas = derivadas

    def parciales(self, funcion):
        x, y = symbols("x y")
        parcial_x = diff(funcion, x)
        parcial_x = parcial_x + y
        derivada = parcial_x.subs(y, funcion)
        return derivada.expand()

    def eval(self,funcion, valor_x, valor_y):
        x, y = symbols("x y")
        return funcion.subs([(x, float(valor_x)), (y, float(valor_y))])

    @property
    def taylor(self):
        if self.n == 0 and self.h == 0:
            #Error! Debes proporcionar un tamaño de paso (h) o una cantidad de puntos (n)
            return "666"

        if self.h == 0:
            self.h = (float(self.xf) - float(self.xi))/self.n

        if self.n == 0:
            self.n = (float(self.xf) - float(self.xi))/self.h

        x = list(np.linspace(float(self.xi), float(self.xf), int(self.n+1)))
        yf = []
        yf.append(self.yi)

        fi = []
        fi.append(self.funct)
        if len(self.derivadas) == 0:
            for i in range(0, self.grado):
                fi.append(self.parciales(fi[-1]))
        else:
            fi += list(map(lambda funct: sympify(funct),self.derivadas))

        for i in range(1, len(x)):
            T = yf[i-1]
            for k in range(len(fi)):
                T += (self.eval(fi[k],x[i-1],yf[i-1]))*(pow(self.h,k+1)/factorial(k+1))
            yf.append(float(T))
        
        resultado = {
            'x': list(map(lambda val: str(val), x)),
            'ytaylor': list(map(lambda val: str(val), yf))
        }

        return resultado