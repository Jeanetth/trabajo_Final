import sympy as sp
import numpy as np

class Hermite:

    def __init__(self,evalu,funct='', xi=[],fi=[],diff=[[]]):
        self.funct = funct
        self.xi = xi
        self.fi = fi
        self.polinomio = []
        self.evaluacion = []
        self.evalu = evalu
        self.diff = diff

    def eval(self, valor):
        x = sp.symbols('x')
        return self.funct.subs(x,float(valor))

    #@property
    def hermite(self):
        x = sp.symbols('x')
        n = len(self.xi)
        if self.funct != "":
            for i in range(0,n):
                self.fi.append(float(self.funct.subs(x,self.xi[i])))

        titulo = ['i   ','xi  ','fi  ']

        ki = np.arange(0,n,1)
        tabla = np.concatenate(([ki],[self.xi],[self.fi]),axis=0)
        tabla = np.transpose(tabla)


        dfinita = np.zeros(shape=(n,n),dtype=float)
        tabla = np.concatenate((tabla,dfinita), axis=1)

        [n,m] = np.shape(tabla)
        diagonal = n-1
        j = 3
        ordenDiff = 1
        while (j < m):

            titulo.append('F['+str(j-2)+']')

            i = 0
            paso = j-2 
            while (i < diagonal):
                denominador = (self.xi[i+paso]-self.xi[i])
                numerador = tabla[i+1,j-1]-tabla[i,j-1]
                if numerador==0 and denominador == 0:
                    tabla[i,j] = self.diff[ordenDiff-1][i]/sp.factorial(ordenDiff)
                else:
                    tabla[i,j] = numerador/denominador
                i = i+1
            ordenDiff= ordenDiff+1
            diagonal = diagonal - 1
            j = j+1


        dDividida = tabla[0,3:]
        n = len(dfinita)

        x = sp.Symbol('x')
        polinomio = self.fi[0]
        for j in range(1,n,1):
            factor = dDividida[j-1]
            termino = 1
            for k in range(0,j,1):
                termino = termino*(x-self.xi[k])
            polinomio = polinomio + termino*factor

        polisimple = polinomio.expand()
        sustitucion = polisimple.subs(x,self.evalu)
        resultado = {
                        "Polinomio": polisimple,
                        "Interpolacion": sustitucion
                    }
        return resultado
#TEST DEL CODIGO PARA EL FRONTEND
"""
Se debe de entregar pares ordenanos en los array xi y fi en el caso de que 
se puede hacer uso de los valores de x y luego calcular dada una funcion 
si no se da una funcion se debe enviar una cadea vacia "" para que no se evalue 
en ninguna funcion.

Como es un metodo que trabaja con derivadas, se debe colocar una matriz respetando 
la derivada de la funcion en dicho punto 

Para mas explicacion se prueba el codigo con un ejercicio de la ingeniera 

REVICE EL PDF:  newton-hermite20abril.pdf en el apartado UNIDAD 4 -> material de clase
"""
xi=[0,0,1,1,1]
fi=[-1,-1,0,0,0]
diff=[[-2,10,10,10,],
      [0, 0, 40, 40]]
resultado=Hermite(4,"d",xi,fi,diff)
print(resultado.hermite())