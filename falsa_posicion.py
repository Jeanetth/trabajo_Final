import sympy as sp
class falsa_posicion:
    def __init__(self, funct, limits, cifras):
        self.funct = sp.sympify(funct.replace("^","**"))
        self.lim_inf = float(limits[0])
        self.lim_sup = float(limits[1])
        self.cifras = cifras
        self.aproximaciones = []
        self.errores = []

    def eval(self, valor):
        x = sp.symbols('x')
        return self.funct.subs(x,float(valor))

    @property
    def falsa_posicion(self):
        Ess = 0.5 * (10**(2 - self.cifras)) # Error de tolerancia
        Ea = 100 # Error aproximado
        xr = 0

        if self.eval(self.lim_inf) * self.eval(self.lim_sup) < 0:
            while Ea > Ess : 
                aproximacionAnterior  = xr

                xr = float(self.lim_inf - (self.eval(self.lim_inf)*(self.lim_inf-self.lim_sup))/((self.eval(self.lim_inf))-self.eval(self.lim_sup)))#Revisar
                self.aproximaciones.append(xr)
                fx1 = self.eval(self.lim_inf)
                fxr = self.eval(xr)
            
                cambiaSigno = (fx1)*(fxr)
            
                if cambiaSigno < 0:
                    self.lim_sup = xr
                if cambiaSigno > 0:
                    self.lim_inf = xr 
                try:
                    Ea = abs((xr -  aproximacionAnterior)/xr)*100
                    self.errores.append(Ea)
                except ZeroDivisionError:
                    resultado = {
                        "Aproximaciones": self.aproximaciones,
                        "Errores": self.errores
                    }
                    return resultado 
        else: 
            return False
        