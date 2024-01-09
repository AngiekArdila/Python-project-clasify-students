import json
import random

path_students = {}
active_students1 = {}
rutas = ["node.js", "java", "netcore"]

with open('active_students.json', 'r') as archivo:
    active_students1 = json.load(archivo)
    print("Archivo leído")

for id, datos in active_students1.items():
    nueva_ruta = random.choice(rutas)  # Use random.choice to select a random element from the list
    datos["nota_final"] = nueva_ruta

# Save the updated active_students dictionary to a file
with open('active_student1.json', 'w') as archivo:
    json.dump(active_students1, archivo, indent=2)
    print("Archivo actualizado active_students")


    