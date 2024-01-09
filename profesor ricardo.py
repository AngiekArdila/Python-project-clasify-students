import json
studentsbase={}
estudiantes_java=[]
estudiantes_node=[]
estudiantes_netcore=[]
#base de datos para profes; indica salon y estudiantes asignados
profesor_ricardo={
"java": estudiantes_java,
"node.js": estudiantes_node,
"netcore": estudiantes_netcore,
}


with open ('studentsbase.json','r')as archivo:
    studentsbase=json.load(archivo)
print("archivo leido con exito")

for id,datos in studentsbase.items():
    if datos["profesores"]=="ricardo-apolo":
        print("porfavor organize sus clases en jornada diurna o nocturna segun su voluntad y ruta asignada")
        if datos["rutas"]=="java":
           estudiantes_java.append(f"{datos['first_name']} {datos['second_name']}, cédula: {id}")
        elif datos["rutas"]=="node.js":
            estudiantes_node.append(f"{datos['first_name']} {datos['second_name']}, cédula: {id}")
        elif datos["rutas"]=="netcore":
            estudiantes_netcore.append(f"{datos['first_name']} {datos['second_name']}, cédula: {id}")

print("\nProfesor Ricardo,usted fue asignado el salón APOLO, y sus estudiantes asignados con ruta JAVA son")
for x in estudiantes_java:
    print(x)

print("\nProfesor Ricardo, usted fue asignado el salon APOLO su salón Apolo, y sus estudiantes asignados con ruta NODE.JS son")
for x in estudiantes_node:
    print(x)

print("\nProfesor Ricardo,usted fue asignado el salón  APOLO, y sus estudiantes asignados con ruta NETCORE son")
for x in estudiantes_netcore:
    print(x)

with open('profesor_ricardo.json','w')as archivo:
    json.dump(profesor_ricardo,archivo)
    print("Archivo exportado profesor_ricardo")
