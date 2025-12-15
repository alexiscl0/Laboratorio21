import math

def area_rectangulo(base, altura):
    return base * altura

def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

def area_circulo(radio):
    return math.pi * radio ** 2

def perimetro_circulo(radio):
    return 2 * math.pi * radio

def area_triangulo(base, altura):
    return (base * altura) / 2


print("Rectángulo (10 x 5):")
print(f"  Área: {area_rectangulo(10, 5)}")
print(f"  Perímetro: {perimetro_rectangulo(10, 5)}")

print("\nCírculo (radio 7):")
print(f"  Área: {area_circulo(7):.2f}")
print(f"  Perímetro: {perimetro_circulo(7):.2f}")

print("\nTriángulo (base 8, altura 6):")
print(f"  Área: {area_triangulo(8, 6)}")