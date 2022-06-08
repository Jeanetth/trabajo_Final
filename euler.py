from sympy import *
import numpy as np
class Euler:

  def __init__(self,xi,yi,xf,h, funct=""):
    self.funct = sympify(funct.replace("^","**"))
    self.xi = xi
    self.yi = yi
    self.xf = xf
    self.h = h
    self.x_n = []
    self.y_n = []

  def eval(self,valorX,valorY):
    x = symbols('x')
    y = symbols('y')
    funciony = self.funct.subs(x,valorX)
    return float(funciony.subs(y,valorY))
  
  def euler(self):
    n=int((self.xf-self.xi)/self.h)  
    x = np.linspace(self.xi, self.xf, int(n+1))                                 
    yf=[]  
    yf.append(self.yi)                                           
    fi = []
    fi.append(self.eval(self.xi,self.yi))                           
    for i in range(0,n):
      yf.append(yf[i]+self.h*fi[i])
      fi.append(self.eval(x[i],yf[i+1]))
      self.x_n.append(x[i+1])
      self.y_n.append(yf[i+1])
    resultado = {
                      "Xn": self.x_n,
                      "Yn": self.y_n
                }
    return resultado
#TEST 

resultado = Euler(0,1,0.5,0.1,"2*x*y")
print(resultado.euler())