from sympy import *

class Newton_Raphson:

    def __init__(self, funct, limits, cifras):
        self.funct = sympify(funct.replace("^","**"))
        self.lim_inf = float(limits[0])
        self.cifras = cifras
        self.aproximaciones = []
        self.errores = []


    def eval(self, valor):
        x = symbols('x')
        return self.funct.subs(x,valor)

    def derivar(self, valor):
        x = symbols('x')
        return diff(self.funct, x).subs(x, valor)


    @property
    def newton_raphson(self):
        Ess = 0.5 * (10**(2 - self.cifras)) # Error de tolerancia
        Ea = 100
        xn = self.lim_inf

        while Ea > Ess:
            anterior = xn
            self.aproximaciones.append(str(xn))

            xn = xn - (self.eval(xn)/self.derivar(xn))

            try:
                Ea = abs((xn - anterior)/xn) * 100
            except ZeroDivisionError:
                resultado = {
                    'Aproximaciones': self.aproximaciones,
                    'Errores': self.errores
                }
                return resultado

            self.errores.append(str(Ea))
        resultado = {
            'Aproximaciones': self.aproximaciones,
            'Errores': self.errores
        }
        return resultado





