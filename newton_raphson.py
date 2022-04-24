import sympy as sp

class Newton_raphson:

    def __init__(self, funct, limits, cifras):
        x = sp.symbols('x')
        self.funct = sp.sympify(funct.replace("^","**"))
        self.derivadaUno = self.funct.diff(x)
        self.derivadaDos = self.derivadaUno.diff(x)
        self.lim_inf = float(limits[0])
        self.cifras = cifras
        self.aproximaciones = []
        self.errores = []

    def eval(self, valor):
        x = sp.symbols('x')
        return self.funct.subs(x,float(valor))

    @property
    def newton_raphson(self):
        Ess = 0.5 * (10**(2 - self.cifras)) # Error de tolerancia
        Ea = 100 # Error aproximado
        xn = 0
        if abs(self.funct.eval(self.lim_inf)*self.derivadaDos.eval(self.lim_inf)/(self.derivadaUno.eval(self.lim_inf)**2))<1:
            while Ea>Ess:#1000>0.05 true
                xn=self.lim_inf
                self.aproximaciones.append(self.lim_inf)
                self.lim_inf = xn-(self.funct(self.lim_inf)/self.funct(self.lim_inf))       
                try:
                    Ea = abs((self.lim_inf - xn)/self.lim_inf)*100
                    self.errores.append(Ea)
                except ZeroDivisionError:
                    resultado = {
                        "Aproximaciones": self.aproximaciones,
                        "Errores": self.errores
                    }
                    return resultado         
        else:
            return False