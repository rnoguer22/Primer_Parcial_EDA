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