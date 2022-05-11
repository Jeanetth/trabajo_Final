from sympy import *
class PuntoFijo:
    def __init__(self, funct, limits, cifras):
        self.funct = sympify(funct.replace("^","**"))#No es la funcion general, es una obtenida a partir de la funcion dada revisar algoritmo si hay duda
        x = symbols('x')
        self.functDerivada = diff(self.funct, x)
        self.lim_inf = float(limits[0])#Solo se necesita un valor inicial 
        self.cifras = cifras 
        self.aproximaciones = []
        self.errores = []

    def eval(self, valor):
        x = symbols('x')
        return self.funct.subs(x,float(valor))

    def punto_fijo(self):
        x = symbols('x')
        Ess = 0.5 * (10**(2 - self.cifras)) # Error de tolerancia
        Ea = 100 # Error aproximado
        xn = self.lim_inf
        if abs(self.functDerivada.subs(x,self.lim_inf))<1:
            while Ea > Ess:
                anterior = xn
                self.aproximaciones.append(xn)
                xn =float(self.eval(xn))
                try:
                    Ea=abs((xn-anterior)/xn)*100
                    self.errores.append(Ea)
                except ZeroDivisionError:
                    return False
            resultado = {
                "Aproximaciones": self.aproximaciones,
                "Errores": self.errores
            } 
            return resultado
        else:
            return False