import math

class Coshx:
    def __init__(self, x, cifras):
        self.x = x
        self.cifras = cifras
        self.aproximaciones = []
        self.errores = []

    @property
    def coshx(self):
        es=(0.5*(10**(2-self.cifras)))
        ea = 1000
        n=1
        aproximacionActual=1
        while ea>es:
            aproximacionAnterior=aproximacionActual
            self.aproximaciones.append(aproximacionActual)
            aproximacionActual=aproximacionActual + math.pow(self.x,2*n)/math.factorial(2*n)
            ea=abs((aproximacionActual-aproximacionAnterior)/aproximacionActual)*100
            self.errores.append(ea)
            n=n+1
        resultado = {
            'Aproximaciones': self.aproximaciones,
            'Errores': self.errores
        }
        return resultado

