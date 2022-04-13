from sympy import *

class Biseccion:
    def __init__(self, funct, limits, cifras):
        self.funct = sympify(funct.replace("^","**"))
        self.lim_inf = float(limits[0])
        self.lim_sup = float(limits[1])
        self.cifras = cifras
        self.aproximaciones = []
        self.errores = []

    def eval(self, valor):
        x = symbols('x')
        return self.funct.subs(x,float(valor))

    @property
    def biseccion(self):
        if self.eval(self.lim_inf) * self.eval(self.lim_sup) < 0:
            Ess = 0.5 * (10**(2 - self.cifras)) # Error de tolerancia
            Ea = 100 # Error aproximado
            aproximacionActual = 0
            while Ea > Ess:
                aproximacionAnterior = aproximacionActual
                aproximacionActual = (self.lim_inf + self.lim_sup)/2
                self.aproximaciones.append(aproximacionActual)
                
                if self.eval(self.lim_inf) * self.eval(aproximacionActual) < 0 :
                    # La raíz se encuentra dentro del subintervalo inferior
                    self.lim_sup = aproximacionActual
                else:
                    # La raíz se encuentra dentro del subintervalo superior
                    self.lim_inf = aproximacionActual
                try:
                    Ea = abs((aproximacionActual -  aproximacionAnterior)/aproximacionActual)*100
                    self.errores.append(Ea)
                except ZeroDivisionError:
                    resultado = {
                        "Aproximaciones": self.aproximaciones,
                        "Errores": self.errores
                    }
                    return resultado   
            resultado = {
                "Aproximaciones": self.aproximaciones,
                "Errores": self.errores
            }
            return resultado
        else:
            return -999





























