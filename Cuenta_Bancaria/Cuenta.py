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

    def ingresar(self):
        dinero_ingresar = 350
        self.saldo += dinero_ingresar

    def transferir(self, dinero_transferir):
        if self.puede_retirar_o_transferir(dinero_transferir):
            "Aqui realizaremos la transferencia"
        else:
            print ("No se pudo retirar dinero")