import json

active_students = {}

ruta_principal = {
    "fundamentos_programacion": {
        "introduccion a los algoritmos": "",
        "pseint": "",
        "python": "",
    },
    "programacion_web": {
        "html": "",
        "css": "",
        "bootsrap": "",
    },
    "programacion_formal": {
        "java": "",
        "javascript": "",
        "c": "",
    },
    "bases_dedatos": {
        "msql": "",
        "mongodb": "",
        "Postgresql": "",
    },
    "backend": {
        "netcore": "",
        "springboot": "",
        "nodejs": "",
        "express": "",
    },
}
print(ruta_principal)

with open('active_students.json', 'r') as archivo:
    active_students = json.load(archivo)
    print("Archivo 'active_students.json' leído:", active_students)

id_consultado = input("Ingresa el id del estudiante al registrar las notas: ")

if id_consultado in active_students:
    print("Estudiante encontrado y activo")

    for temaprincipal, subtemas in ruta_principal.items():
        print(f"Ingrese las notas para el temaprincipal '{temaprincipal}':")

        for subtema in subtemas:
            nota1 = float(input(f"ingrese la nota PRACTICA para el subtema'{subtema}:"))
            nota2 = float(input(f"Ingrese la nota TEORICA para el subtema '{subtema}':"))

            nota1 = nota1 * 0.6
            nota2 = nota2 * 0.4
            nota = nota1 + nota2

            print(nota)

            ruta_principal[temaprincipal][subtema] = nota  

    with open('ruta_principalnotas.json', 'w') as archivo:
        json.dump(ruta_principal, archivo, indent=2)
    
    print("Archivo exportado")
else:
    print("Estudiante no encontrado o inactivo")

for student_id, datos in active_students.items():
    if student_id == id_consultado:
        datos["rutas_notashistoria"] = ruta_principal

with open('active_notasrutas.json', 'w') as archivo:
    json.dump(active_students, archivo, indent=2)
    print("Archivo creado active_notasrutas")
