import math

cifras = -1
ea = 1000
while cifras < 0:
    cifras = int(input("Ingrese la cantidad de cifras"))
    if cifras < 0:
        print("No se puede efectuar")
    else:
        es = 0.5*(10**(2-cifras))

valorDeX = math.pi/8
n = 0
aproximacionActual = 0

while ea > es: 
    aproximacionAnterior = aproximacionActual
    aproximacionActual = aproximacionActual + (math.pow(valorDeX,(2*n+1))/math.factorial(2*n+1))
    ea = abs((aproximacionActual-aproximacionAnterior)/aproximacionActual)*100
    n = n + 1

print("El valor es ", aproximacionActual)
print("El error es ", ea)
