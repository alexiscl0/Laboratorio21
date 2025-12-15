import json

equipos = [
    {"Nombre": "Real Madrid", "pais": "España", "nivelAtaque": 92, "nivelDefensa": 88},
    {"Nombre": "Barcelona", "pais": "España", "nivelAtaque": 90, "nivelDefensa": 85},
    {"Nombre": "Manchester City", "pais": "Inglaterra", "nivelAtaque": 94, "nivelDefensa": 89},
    {"Nombre": "Bayern Munich", "pais": "Alemania", "nivelAtaque": 91, "nivelDefensa": 87},
    {"Nombre": "PSG", "pais": "Francia", "nivelAtaque": 93, "nivelDefensa": 84},
]

for equipo in equipos:
    print(f"{equipo['Nombre']} ({equipo['pais']}) - "
          f"Ataque: {equipo['nivelAtaque']}, Defensa: {equipo['nivelDefensa']}")

json_texto = json.dumps(equipos, indent=2)
print(json_texto)

with open("equipos.json", "w", encoding="utf-8") as archivo:
    archivo.write(json_texto)

print("\nGuardado en equipos.json")