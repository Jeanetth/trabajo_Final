from math import factorial
import math

cifras =-1
ea=1000   
#dos puntos al final de los if while etc
#identacion

while cifras<0:
    cifras =int(input("ingrese la cantidade cifras"))
    if cifras<0:
        print ("No se puede efectuar")
    else:
        es=(0.5*(10**(2-cifras)))#hasta aca  obtengo ES mi formula de comparacion
valorDex=math.pi/8 #declaracion de variablesy metodo
n=0
aproximacionActual=0
while ea>es:
    aproximacionAnterior=aproximacionActual
    aproximacionActual=aproximacionActual + math.pow(valorDex,2*n)/math.factorial(2*n)
    ea=abs((aproximacionActual-aproximacionAnterior)/aproximacionActual)*100
    n=n+1
     
print ("El valor es",aproximacionActual)
print ("El resultado es",ea)