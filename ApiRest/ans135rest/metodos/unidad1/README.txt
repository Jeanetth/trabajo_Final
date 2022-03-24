Clases:
sinx.py
cosx.py
sinhx.py
coshx.py
arcsinx.py
arctgx.py
lnfun.py

NOTA: Para facilitar y agilizar el acoplamiento con la vista, recuerden que cada archivo .py debe tener
la siguiente estructura:

class Sinx:
   # El constructor debe solicitar los parámetros
   # necesarios para poder hacer los calculos
   def __init__(self, *args):
	#code...	
   
   # debe llevar un método con el mismo nombre de la clase

   @property
   def sinx(self):
	#code...
