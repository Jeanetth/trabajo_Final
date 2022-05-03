import sympy as sp
import numpy as np

class Lagrange:
    def __init__(self, funct, xi, fi,evalu):
        self.funct = funct
        self.xi = xi
        self.fi = fi
        self.polinomio = []
        self.evaluacion = []
        self.evalu = evalu
    
    def eval(self, valor):
        x = sp.symbols('x')
        return self.funct.subs(x,float(valor))

    @property
    def lagrange(self):
        x = sp.symbols('x')
        n = len(self.xi)
        if len(self.funct) != 0:
            self.funct = sp.sympify(self.funct.replace("^","**"))
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
                        "Aproximaciones": polisimple,
                        "Errores": sustitucion
                    }
        return resultado
