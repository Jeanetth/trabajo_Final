from sympy import *
import numpy as np

class Lagrange:
    def __init__(self,xi,evalu,funct='', fi=[]):
        self.funct = funct
        self.xi = xi
        self.fi = fi
        self.polinomio = []
        self.evaluacion = []
        self.evalu = evalu
    
    def eval(self, valor):
        x = symbols('x')
        return self.funct.subs(x,float(valor))

    @property
    def lagrange(self):
        x = symbols('x')
        n = len(self.xi)
        if len(self.funct) != 0:
            self.funct = sympify(self.funct.replace("^","**"))
            self.fi = []
            for i in range(0,n):
                self.fi.append(float(self.eval(self.xi[i])))
        polinomio = 0
        divisorL = np.zeros(n, dtype = float)
        for i in range(0,n,1):
            numerador = 1
            denominador = 1
            for j  in range(0,n,1):
                if (j!=i):
                    numerador = numerador*(x-self.xi[j])
                    denominador = denominador*(self.xi[i]-self.xi[j])
            terminoLi = numerador/denominador
            polinomio = polinomio + terminoLi*self.fi[i]
            divisorL[i] = denominador
        polisimple = polinomio.expand()
        sustitucion = polisimple.subs(x,self.evalu)
        resultado = {
                        "Polinomio": polisimple,
                        "Interpolacion": sustitucion
                    }
        return resultado


xi = [-2,-1,1,2]
fi = [-9,8,0,-1]

respuesta = Lagrange(xi= xi, fi= fi, evalu=1).lagrange

print(respuesta)
