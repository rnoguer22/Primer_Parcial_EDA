from Cuenta_Bancaria.Cuenta import Cuenta_Bancaria

class Plazo_Fijo(Cuenta_Bancaria):
    #Esta clase es heredada de Cuenta_Bancaria
    def __init__(self, id_cuenta, nombre, fecha_apertura, num_cuenta, saldo):
        super().__init__(id_cuenta, nombre, fecha_apertura, num_cuenta, saldo)
    
    def retirar_dinero(self, dinero):

        #Funcion para calcular la pena por vencimiento
        def penalizacion(money):
            money += 0.05*money
            return money

        Cuenta_Bancaria.retirar(dinero)
        vencimiento = self.fecha_apertura + 9   #Damos 9 meses de vencimiento
        fecha_retirar = 13

        #Condicional para hallar el saldo que nos queda
        if fecha_retirar < vencimiento:
            retiro = penalizacion(dinero)
            self.saldo -= retiro
        else:
            self.saldo -= dinero

        #Nos aseguramos que el saldo de este tipo de cuenta no puede ser menor que cero
        if self.saldo <= 0:
            self.saldo = 0
        else: pass
        print ("Su saldo restante es {}€".format(self.saldo))

    def ingresar_dinero(self, dinero):
        Cuenta_Bancaria.ingresar(dinero)
    
    def transferir_dinero(self, dinero):
        Cuenta_Bancaria.transferir(dinero)
