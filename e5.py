# Ejercicio 5: Calculadora con excepciones

class OperadorInvalidoError(Exception):
    pass

def calcular(operacion):
    try:
        resultado = None
        partes = operacion.split()
        
        num1 = float(partes[0])
        operador = partes[1]
        num2 = float(partes[2])
        
        if operador not in ['+', '-', '*', '/']:
            raise OperadorInvalidoError(f"Operador '{operador}' no válido")
        
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                resultado = None
            else:
                resultado = num1 / num2
        
        if resultado is None:
            return "Error: No puedes dividir entre cero"
        return f"{num1} {operador} {num2} = {resultado}"
    
    except ValueError:
        return "Error: Los valores deben ser números"
    except OperadorInvalidoError as e:
        return f"Error: {e}"
    except IndexError:
        return "Error: Formato debe ser 'numero operador numero'"


print(calcular("10 / 2"))
print(calcular("15 + 25"))
print(calcular("10 / 0"))
print(calcular("abc + 5"))
print(calcular("10 % 3"))