class Libro:
    #Definimos el constructor
    def __init__(self, nombre, autor, isbn, fecha_publicacion):
        self.nombre = nombre
        self.autor = autor
        self. isbn = isbn
        self.fecha_publicacion = fecha_publicacion

    def get_nombre(self):
        return self.nombre
    
    def get_autor(self):
        return self.autor
    
    def get_isbn(self):
        return self.isbn
    
    def get_fecha_publicacion(self):
        return self.fecha_publicacion