import random
import json

def create_students_base():
    students = {}
    names = ["Camila", "maria", "teresa", "marcos", "Ivan", "michael", "cristopher"]
    lastnames = ["ardila", "lopez", "mejia", "aguilera", "perez", "quitian", "hemsworth"]
    adresses = ["laconcordia", "floridablanca", "giron", "ruitoque", "provenza", "realdeminas", "salitre"]
    emergency = ["Irma", "victoria", "monica", "chandler", "robert", "pattinson", "pablo"]
    cellphone = ["3102054388", "452317856", "485955966", "4859999994", "788888778"]
    estado = ["activo", "inactivo"]
    profesoresysalones=["camilo-sputnik","ricardo-apolo","arturo-artemis","jaime-sputnik"]
    fechainicioyfinal=["enero2024-octubre2024","junio2024-marzo2024","diciembre2024-septimebre2024"]
    rutas = ["node.js", "java", "netcore"]
    

    

    for i in range(100):
        student_id = i + 1
        obj = {
            "id_number": student_id,
            "first_name": names[random.randint(0, 6)],
            "second_name": lastnames[random.randint(0, 6)],
            "address": adresses[random.randint(0, 6)],
            "emergency_contact": emergency[random.randint(0, 6)],
            "cellphone": cellphone[random.randint(0, 4)],
            "estado_student": estado[random.randint(0, 1)],
            "profesores": profesoresysalones[random.randint(0,3)],
            "fechainicioyfinal":fechainicioyfinal[random.randint(0,2)],
            "rutas":rutas[random.randint(0,2)]
            
             
        }
         # Corregido: añadida coma al final
        students[student_id] = obj

    return students

studentsbase = create_students_base()

with open('studentsbase.json', 'w') as archivo:
    json.dump(studentsbase, archivo, indent=2)
    print("El archivo ha sido exportado")