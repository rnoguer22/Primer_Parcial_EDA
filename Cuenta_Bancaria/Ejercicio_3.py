from random import randint

class Cuenta_Bancaria:
    #Constructor
    def __init__(self, id_cuenta, nombre, fecha_apertura, num_cuenta, saldo):
        self.id_cuenta = id_cuenta
        self.nombre = nombre
        self.fecha_apertura = fecha_apertura
        self.num_cuenta = num_cuenta
        self.saldo = saldo

    #Funcion para saber si podemos retirar o transferir dinero
    def puede_retirar_o_transferir(self, dinero):
        if dinero > self.saldo:
            print ("No se pudo realizar la operacion")
            return False
        else:
            print ("La operacion se ha ralizado correctamente")
            return True

    def retirar(self, dinero_retirar):
        if self.puede_retirar_o_transferir(dinero_retirar):
            self.saldo -= dinero_retirar
        else:
            print ("No se pudo retirar dinero :(")

    def ingresar(self, dinero_ingresar):
        self.saldo += dinero_ingresar
        print ("Ha ingresado {}€. Su saldo actual es de {}€".format(dinero_ingresar, self.saldo))

    def transferir(self, dinero_transferir, cuenta_a_transferir):
        if self.puede_retirar_o_transferir(dinero_transferir):
            self.saldo -= dinero_transferir
            cuenta_a_transferir.saldo += dinero_transferir
            print ("Se han transferido {}€ de {} a {}".format(dinero_transferir,Cuenta_Bancaria, cuenta_a_transferir))
        else:
            print ("No se pudo transferir el dinero")

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
    
    def transferir_dinero(self, dinero, cuenta_a_transferir):
        Cuenta_Bancaria.transferir(dinero, cuenta_a_transferir)

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
    
    def transferir_dinero(self, dinero, cuenta_a_transferir):
        Cuenta_Bancaria.transferir(dinero, cuenta_a_transferir)


#Definimos las instancias de clases
cuenta_bancaria = Cuenta_Bancaria (1, "Ruben", 9, 10, 10000)
cuenta_plazo_fijo = Plazo_Fijo (2, "Moyis", 3, 5, 10000)   #Eliminamos los randint que pueden dar problemas si coinciden
cuenta_vip = Cuenta_Vip (3, "Malaguita", 7, 3, 10000, -500)

#Realizamos una transferencia
cuenta_plazo_fijo.transferir_dinero(2000, cuenta_vip)

#Realizamos un ingreso de dinero
cuenta_bancaria.ingresar(575)

#Realizamos una retirada de dinero
cuenta_vip.retirar_dinero_vip(78)