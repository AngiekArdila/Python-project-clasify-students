import json

studentsbase = {}
active_students = {}

with open('studentsbase.json', 'r') as archivo:
    studentsbase = json.load(archivo)
    print("Archivo leído")

print(studentsbase)

for id, datos in studentsbase.items():
    if datos["estado_student"] == "activo":
        print("Este estudiante está activo y este es su identificación:", id)
        print("Estos son los datos completos del estudiante", datos)
        active_students[id] = datos

# Save the active_students dictionary to a file after the loop
with open('active_students.json', 'w') as archivo:
    json.dump(active_students, archivo, indent=2)
    print("Archivo generado active_students")