from random import randint

"Hay un error con los import, no se importan correctamente, no encuentro el fallo"
"Para ello se encuentra el archivo Ejercicio_3.py en el que esta todo el contenido sin importaciones"

from Cuenta_Bancaria.Cuenta import *
from Cuenta_Bancaria.Plazo_fijo import *
from Cuenta_Bancaria.Vip import *

if __name__ == '__main__':
    
    #Definimos las instancias de clases
    cuenta_bancaria = Cuenta_Bancaria (1, "Ruben", 9, 10, 10000)
    cuenta_plazo_fijo = Plazo_Fijo (2, "Moyis", 3, 5, 10000)
    cuenta_vip = Cuenta_Vip (3, "Malaguita", 7, 3, 10000)

    #Realizamos una transferencia
    cuenta_plazo_fijo.transferir_dinero(2000, cuenta_vip)

    #Realizamos un ingreso de dinero
    cuenta_bancaria.ingresar(575)

    #Realizamos una retirada de dinero
    cuenta_vip.retirar_dinero_vip(78)