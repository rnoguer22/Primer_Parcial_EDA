#Definimos las clases asi como sus constructores
class Animal:
    def __init__(self, especie):
        self.especie = especie

class Mamifero(Animal):
    def __init__(self, especie, mamifero):
        super().__init__(especie)
        self.mamifero = mamifero
class Oviparo(Mamifero):
    def __init__(self, especie, mamifero, oviparo):
        super().__init__(especie, mamifero)
        self.oviparo = oviparo

#Declaramos las instancias de clase
pollo = Animal("pollo")
gato = Mamifero("gato", True)
ornitorrinco = Oviparo("ornitorrinco", True, True)

#Vemos que el ornitorrinco es un mamifero...
print (ornitorrinco.mamifero)