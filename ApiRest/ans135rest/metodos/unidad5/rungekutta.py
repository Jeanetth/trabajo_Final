from math import *

class Rungekutta:
    def __init__(self,x0,xf,y0,f,n):
        self.x0 = x0
        self.xf = xf
        self.y0 = y0
        self.f = f
        self.n = n
   
    def rungekutta2(self):
        h = (self.xf - self.x0)/self.n
        t = self.x0
        w = self.y0
        resultado = ("x0 = {0:.2f}, y0 = {1:.12f}\n".format(t, w))
        
        for i in range(1, self.n+1): 
            k1 = self.f(t, w)
            k2 = self.f(t + h, w + k1*h)
            w = w + h*(k1 + k2)/2
            t = self.x0 + i*h
            resultado = resultado + ("x{0:<2} = {1:.2f}, y{0:<2} = {2:.12f}\n".format(i, t, w))
        
        return resultado

    def rungekutta3(self):
        h = (self.xf - self.x0)/self.n
        t = self.x0
        w = self.y0
        resultado = ("x0 = {0:.2f}, y0 = {1:.12f}\n".format(t, w))
        
        for i in range(1, self.n+1): 
            k1 = self.f(t, w)
            k2 = self.f(t + h/2, w + h*k1/2)
            k3 = self.f(t + h, w - k1*h + 2*k2*h)
            w = w + h*(k1 + 4*k2 + k3)/6
            t = self.x0 + i*h
            resultado = resultado + ("x{0:<2} = {1:.2f}, y{0:<2} = {2:.12f}\n".format(i, t, w))
        
        return resultado  
  
    def rungekutta4(self):
        h = (self.xf - self.x0)/self.n
        t = self.x0
        w = self.y0
        resultado = ("x0 = {0:.2f}, y0 = {1:.12f}\n".format(t, w))
        
        for i in range(1, self.n+1): 
            k1 = h*self.f(t, w)
            k2 = h*self.f(t + h/2, w + k1/2)
            k3 = h*self.f(t + h/2, w + k2/2)
            k4 = h*self.f(t + h, w + k3)
            w = w + (k1 + 2*k2 + 2*k3 + k4)/6           
            t = self.x0 + i*h
            resultado = resultado + ("x{0:<2} = {1:.2f}, y{0:<2} = {2:.12f}\n".format(i, t, w))
        
        return resultado    