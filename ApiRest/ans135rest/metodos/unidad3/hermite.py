from sympy import *
from functools import reduce

class Hermite:
    def __init__(self, x,interpolado, funct="", y = [], dy =[]):
        self.x = x
        self.interpolado = sympify(interpolado)
        self.funct = sympify(funct.replace("^","**")) if funct != "" else ""
        self.y = y
        self.dy = dy
        self.diferencias = []
        self.resultado = {}

    def eval(self,valor):
        x = symbols('x')
        self.funct = sympify(self.funct)
        return self.funct.subs(x, float(valor))
    
    def evaldif(self, valor):
        x = symbols('x')
        self.funct = sympify(self.funct)
        derivada = diff(self.funct, x)
        return derivada.subs(x, float(valor))
    
    def calcular_diferencias(self,tabla, expansion):
        nueva_tabla = []
        self.diferencias.append(tabla[0])

        for k in range(1, len(tabla)):
            calc = (tabla[k]-tabla[k-1])/(self.x[k+expansion] - self.x[k-1])
            nueva_tabla.append(float(calc))

        if len(nueva_tabla) >= 1:
            expansion += 1
            self.calcular_diferencias(nueva_tabla,expansion)

    @property
    def hermite(self):
        x = symbols('x')
        if self.funct != "":
            for valor in self.x:
                self.y.append(self.eval(valor))
                self.dy.append(self.evaldif(valor))
        tab = 0
        for i in range(len(self.dy)):
            if self.dy[i] != None:
                #si existe valor de la primer derivda para este valor de x, de duplica
                self.x.insert(i+tab, self.x[i+tab])
                self.y.insert(i+tab, self.y[i+tab])
            tab += 1
        #la primer diferencia dividida es f(x0)
        self.diferencias.append(self.y[0])

        tabla = []

        tab = 1
        for k in range(1, len(self.y)):
            if (self.x[k]-self.x[k-1]) == 0:
                calc = self.dy[k-tab]
                tab += 1
            else:
                calc = (self.y[k]-self.y[k-1])/(self.x[k]-self.x[k-1])
            tabla.append(float(calc))
        
        self.calcular_diferencias(tabla,1)

        factores = []
        factores.append(self.diferencias[0])
        factor = 1

        for i in range(1, len(self.x)):
            factor = factor * (x - float(self.x[i-1]))
            factores.append(self.diferencias[i] * factor)
        
        polinomio = reduce(lambda x,y: x + y, factores)
        polinomio = polinomio.expand()

        interpolacion = polinomio.subs(x, self.interpolado)
        interpolacion = float(interpolacion)
        self.resultado['Polinomio'] = [str(polinomio).replace("**","^")]
        self.resultado['Interpolado'] = [str(interpolacion)]

        return self.resultado
