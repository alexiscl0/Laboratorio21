class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = True
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False
    
    def devolver(self):
        self.disponible = True


class LibroDigital(Libro):
    def __init__(self, titulo, autor, año, formato, tamañoMB):
        super().__init__(titulo, autor, año)
        self.formato = formato
        self.tamañoMB = tamañoMB


class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def listar_libros(self):
        for libro in self.libros:
            estado = "Disponible" if libro.disponible else "Prestado"
            print(f"{libro.titulo} - {libro.autor} ({libro.año}) [{estado}]")
    
    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.prestar():
                    print(f"Libro prestado: {titulo}")
                else:
                    print(f"Libro no disponible: {titulo}")
                return
        print(f"Libro no encontrado: {titulo}")
    
    def buscar_por_autor(self, autor):
        print(f"Libros de {autor}:")
        for libro in self.libros:
            if autor in libro.autor:
                print(f"  - {libro.titulo}")

biblioteca = Biblioteca()

libro1 = Libro("Don Quijote", "Cervantes", 1605)
libro2 = Libro("Cien años de soledad", "García Márquez", 1967)
libro3 = LibroDigital("El principito", "Saint-Exupéry", 1943, "PDF", 2.5)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

print("=== LIBROS ===")
biblioteca.listar_libros()

print("\n=== PRESTAR LIBRO ===")
biblioteca.prestar_libro("Don Quijote")

for i in range(5):
    biblioteca.prestar_libro("El principito")

biblioteca.buscar_por_autor("García Márquez")

