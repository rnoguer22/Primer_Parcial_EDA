from Cuenta_Bancaria.Cuenta import Cuenta_Bancaria
from Cuenta_Bancaria.Plazo_fijo import Plazo_Fijo 

class Cuenta_Vip(Plazo_Fijo):
    #Definimos el constructor
    def __init__(self, id_cuenta, nombre, fecha_apertura, num_cuenta, saldo, saldo_negativo_max):
        super().__init__(id_cuenta, nombre, fecha_apertura, num_cuenta, saldo)
        #Agregamos el nuevo atributo
        self.saldo_negativo_max = saldo_negativo_max
    
    def retirar_dinero_vip(self, dinero):
        Cuenta_Bancaria.retirar(dinero)
        #De la siguiente manera nos aseguramos que el saldo no sea inferior que el valor minimo negativo
        if self.saldo < self.saldo_negativo_max:
            self.saldo = self.saldo_negativo_max
            print ("Su saldo ha alcanzado su valor negativo maximo, {}€".format(self.saldo))
        else:
            pass

    def ingresar_dinero_vip(self, dinero):
        Cuenta_Bancaria.ingresar(dinero)
    
    def transferir_dinero(self, dinero):
        Cuenta_Bancaria.transferir(dinero)
