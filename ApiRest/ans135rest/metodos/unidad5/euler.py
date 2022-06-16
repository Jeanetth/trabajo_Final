from sympy import *
import numpy as np

class Euler:
  def __init__(self,funct, xi, yi,xf, h="",n=""):
    self.funct = sympify(funct.replace("^","**"))
    self.xi = sympify(xi)
    self.yi = sympify(yi)
    self.xf = sympify(xf)
    self.h = h
    self.n = n

  def eval(self, valorX, valorY=""):
    x,y = symbols('x y')
    if "y" not in str(self.funct):
      return self.funct.subs(x, float(valorX))
    else:
      return self.funct.subs([(x, float(valorX)),(y, float(valorY))])

  @property
  def euler(self):

    if self.h == "" and self.n == "":
      return "666"

    if self.h == "":
      self.h = (self.xf - self.xi)/self.n

    if self.n == "":
      self.n = (self.xf - self.xi)/self.h

    x = list(np.linspace(float(self.xi), float(self.xf), int(self.n+1)))
    yf = []
    yf.append(self.yi)

    for i in range(1, len(x)):
      if "y" not in str(self.funct):
        yf.append(yf[i-1]+(self.eval(x[i-1])*self.h))
      else:
        yf.append(yf[i-1]+(self.eval(x[i-1],yf[i-1])*self.h))

    resultado = {
      'x': list(map(lambda valor: str(valor),x)),
      'yeuler': list(map(lambda valor: str(valor), yf))
    }

    return resultado