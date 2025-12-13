class libros:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.disponible = True

    def descripcion(self):
        return f"'{self.titulo}' es un libro escrito por {self.autor} en {self.anio_publicacion}."

class Libro_Digital(libros):
    def __init__(self, titulo, autor, anio_publicacion, formato):
        super().__init__(titulo, autor, anio_publicacion)
        self.formato = formato
        self.genero = "Digital"

    def descripcion(self):
        return f"'{self.titulo}' es un libro digital en formato {self.formato}, escrito por {self.autor} en {self.anio_publicacion}."