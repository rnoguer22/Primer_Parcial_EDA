class Cuenta_Bancaria:
    #Constructor
    def __init__(self, id_cuenta, nombre, fecha_apertura, num_cuenta, saldo):
        self.id_cuenta = id_cuenta
        self.nombre = nombre
        self.fecha_apertura = fecha_apertura
        self.num_cuenta = num_cuenta
        self.saldo = saldo

    def retirar_dinero(self):
        dinero_retirar = 70
        self.saldo -= dinero_retirar

    def ingresar_dinero(self):
        dinero_ingresar = 350
        self.saldo += dinero_ingresar

    def transferir_dinero(self):