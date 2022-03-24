from random import randint

from Cuenta_Bancaria.Cuenta import Cuenta_Bancaria
from Cuenta_Bancaria.Plazo_fijo import Plazo_Fijo
from Cuenta_Bancaria.Vip import Cuenta_Vip

#Definimos las instancias de clases
cuenta_bancaria = Cuenta_Bancaria (1, "Ruben", 9, randint(1,12), 10000)
cuenta_plazo_fijo = Plazo_Fijo (2, "Moyis", 3, randint(1,12), 10000)
cuenta_vip = Cuenta_Vip (3, "Malaguita", 7, randint(1,12), 10000)