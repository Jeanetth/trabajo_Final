import sympy as sp
class Punto_fijo:
    def __init__(self, funct, limits, cifras):
        self.funct = sp.sympify(funct.replace("^","**"))#No es la funcion general, es una obtenida a partir de la funcion dada revisar algoritmo si hay duda
        x = sp.symbols('x')
        self.functDerivada = self.funct.diff(x)
        self.lim_inf = float(limits[0])#Solo se necesita un valor inicial 
        self.cifras = cifras 
        self.aproximaciones = []
        self.errores = []

    def eval(self, valor):
        x = sp.symbols('x')
        return self.funct.subs(x,float(valor))

    def punto_fijo(self):
        x = sp.symbols('x')
        Ess = 0.5 * (10**(2 - self.cifras)) # Error de tolerancia
        Ea = 100 # Error aproximado
        if abs(self.functDerivada.subs(x,self.lim_inf))<1:
            while Ea > Ess:
                xn=self.lim_inf
                self.aproximaciones.append(xn)
                self.lim_inf=float(self.eval(self.lim_inf))
            try:
                Ea=abs((self.lim_inf-xn)/self.lim_inf)*100
                self.errores.append(Ea)
            except ZeroDivisionError:
                resultado = {
                    "Aproximaciones": self.aproximaciones,
                    "Errores": self.errores
                }
                return resultado 
        else:
            return False