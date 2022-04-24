import sympy as sp 

class Secante:
    
    def __init__(self, funct, limits, cifras): 
        self.funct = sp.sympify(funct.replace("^","**"))
        self.lim_inf = float(limits[0])
        self.lim_sup=float(limits[1])
        self.cifras = cifras
        self.aproximaciones = []
        self.errores = []

    def eval(self, valor):
        x = sp.symbols('x')
        return self.funct.subs(x,float(valor))
        
        
    @property
    def secante(self):
        Ess = 0.5 * (10**(2 - self.cifras)) # Error de tolerancia
        ea = 100 # Error aproximado

        if self.funct.eval(self.lim_inf)*self.funct.eval(self.lim_sup) < 0 :
            xn_mas_uno = 0
            while ea >= Ess: 
                aproximacionAnterior = xn_mas_uno
                xn_mas_uno = float(self.lim_sup-self.eval(self.lim_sup)*((self.lim_sup-self.lim_inf)/(self.funct.eval(self.lim_sup)-self.funct(self.lim_inf))))
                self.lim_inf = self.lim_sup
                self.lim_sup =xn_mas_uno
                
                try:
                    ea = abs((xn_mas_uno-aproximacionAnterior)/xn_mas_uno)*100   
                    self.errores.append(ea)
                except ZeroDivisionError:
                    resultado = {
                        "Aproximaciones": self.aproximaciones,
                        "Errores": self.errores
                    }
                    return resultado 
        else: 
            return False