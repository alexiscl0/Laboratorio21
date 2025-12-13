import math
class Triangulo:
    def __init__(self):
        self.nombre = "Triangulo"
        print(f"=" * 10 + self.nombre + "=" * 10)
        self.base = int(input("Ingrese la base del triangulo: "))
        self.lado1 = int(input("Ingrese el lado 1 del triangulo: "))
        self.lado2 = int(input("Ingrese el lado 2 del triangulo: "))
        self.altura = int(input("Ingrese la altura del triangulo: "))
    def area(self):
        area= (self.base * self.altura) / 2
        return area
    def perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.base
        return perimetro

class Circulo:
    def __init__(self):
        self.nombre = "Circulo"
        print(f"=" * 10 + self.nombre + "=" * 10)
        self.radio = int(input("Ingrese el radio del circulo: "))
    def area(self):
        area = math.pi * (self.radio ** 2)
        return area
    def perimetro(self):
        perimetro= 2 * math.pi * self.radio
        return perimetro

class Rectangulo:
    def __init__(self):
        self.nombre = "Rectangulo"
        print(f"=" * 10 + self.nombre + "=" * 10)
        self.base = int(input("Ingrese la base del rectangulo: "))
        self.altura = int(input("Ingrese la altura del rectangulo: "))
    def area(self):
        area = self.base * self.altura
        return area
    def perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        return perimetro

r=Rectangulo()
c=Circulo()
t=Triangulo()
figuras = [r, c, t]
for figura in figuras:
    print(f"\nFigura: {figura.nombre}")
    print(f"- Area: {figura.area()}")
    print(f"- Perimetro: {figura.perimetro()}")