Clases:
biseccion.py
falsa_posicion.py
punto_fijo.py
newton_raphson.py
secante.py
bairstow.py
muller.py

NOTA: para facilitar y agilizar el acoplamiento con la vista, cada archivo .py debe tener
la siguiente estructura:

# Una clase con el mismo nombre que el archivo

class Metodo:
   # El constructor debe solicitar la expr a evaluar
   # Ejemplo: 'exp(x) + x'
   # y los parametros necesarios para realizar los calculos adecuadamente
   def __init__(self, expr, *args):
	#code...

   # Un método con el mismo nombre de la clase pero en minúsculas
   # que se encargue de ralizar todas las operaciones
   # debe devolver una lista con los resultados, aunque solamente sea uno
   @property
   def metodo(self):
	#code...
