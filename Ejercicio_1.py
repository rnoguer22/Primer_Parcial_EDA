class Libro:
    #Definimos el constructor
    def __init__(self, titulo, autor, isbn, fecha_publicacion):
        self.titulo = titulo
        self.autor = autor
        self. isbn = isbn
        self.fecha_publicacion = fecha_publicacion

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_isbn(self):
        return self.isbn
    
    def get_fecha_publicacion(self):
        return self.fecha_publicacion

libro = Libro("Harry Potter", "J.K. Rowling", 217328723, "13/09/2001")

print ("El libro que ha seleccionado es {} y su autor es {}.".format(libro.get_titulo(), libro.get_autor()))