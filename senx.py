from math import factorial
import math

cifras =-1
ea=1000   


while cifras<0:
    cifras =int(input("ingrese la cantidade cifras"))
    if cifras<0:
        print ("No se puede efectuar")
    else:
        es=(0.5*(10**(2-cifras)))

valorDex=math.pi 
n=3
signo = 1
aproximacionActual=valorDex

while ea>es:
    aproximacionAnterior=aproximacionActual

    if signo % 2 == 0:
        print("par")
        aproximacionActual=aproximacionActual + math.pow(valorDex,n)/math.factorial(n)
    else:
        aproximacionActual=aproximacionActual - math.pow(valorDex,n)/math.factorial(n)
        print("impar")
    ea=abs((aproximacionActual-aproximacionAnterior)/aproximacionActual)*100
    n=n+2
    signo = signo+1
     
print ("El valor es",aproximacionActual)
print ("El resultado es",ea)