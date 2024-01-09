import json

while True:
        saludo = int(input("""
        Bienvenido al programa de Campusland
        -Por cierto nos alegra tenerte aquí!
        (seleccione una opción por favor)

        (1) Visualizar estudiante por ID y su información
        (2) Ver lista de estudiantes activos-admitidos
        (3) Ingresar notas de estudiante-admitido por cada ítem
        (4) Para profesores: Ver estudiantes asignados, rutas y salón
        (5) Ver estudiantes asignados por rutas (Java, Node.js, NetCore)
        (6) Ver historial de notas
        (7) Graduados de CampusLands (Estudiantes que aprobaron el curso al final)
        (8) SALIR
        """))

        if saludo == 1:
            print("¡Hola! A continuación verás la información del estudiante en nuestra base de datos.")
            active_students = {}
            with open('studentsbase.json', 'r') as archivo:
                studentsbase = json.load(archivo)
            id_ingresado = input("Ingresa el ID del estudiante: ")
            for id, datos in studentsbase.items():
                if id == id_ingresado:
                    print(f"Este estudiante está activo y este es su identificación: {id}")
                    print("Estos son los datos completos del estudiante:", datos)

        elif saludo == 2:
            print("A continuación verás la lista de estudiantes admitidos/activos:")
            with open('active_students.json', 'r') as archivo:
                active_students = json.load(archivo)
                print(active_students)

        elif saludo == 3:
            print("Ingresarás las notas de los estudiantes. Sigue las instrucciones.")
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
            with open('active_students.json', 'r') as archivo:
                active_students = json.load(archivo)
            id_consultado = input("Ingresa el id del estudiante al registrar las notas: ")
            if id_consultado in active_students:
                print("Estudiante encontrado y activo")
                for temaprincipal, subtemas in ruta_principal.items():
                    print(f"Ingrese las notas para el temaprincipal '{temaprincipal}':")
                    for subtema in subtemas:
                        nota1 = float(input(f"Ingrese la nota PRACTICA para el subtema '{subtema}':"))
                        nota2 = float(input(f"Ingrese la nota TEORICA para el subtema '{subtema}':"))
                        nota1 = nota1 * 0.6
                        nota2 = nota2 * 0.4
                        nota = nota1 + nota2
                        todas_notas = []
                        print(f"Esta es la nota general del subtema'{subtema}':", nota)
                        ruta_principal[temaprincipal][subtema] = nota  
                        todas_notas.append(nota)
                with open('ruta_principalnotas.json', 'w') as archivo:
                    json.dump(ruta_principal, archivo, indent=2)
                print("Archivo Almacenado")
            else:
                print("Estudiante inactivo")
            for student_id, datos in active_students.items():
                if student_id == id_consultado:
                    sum_todas_notas = sum(todas_notas)
                    print("\nPROMEDIO GENERAL DEL ESTUDIANTE : ", sum_todas_notas)
                    datos["rutas_notashistoria"] = ruta_principal
                    datos["Nota_final"] = sum_todas_notas
            with open('active_notasrutas.json', 'w') as archivo:
                json.dump(active_students, archivo, indent=2)
                print("\nFELICIDADES se ha cargado a la base de datos del estudiante")
            
        elif saludo == 4:
            print("Profesor, a continuación podrás ver tus estudiantes asignados ordenados por rutas, salón e ID.")
            print("IMPORTANTE por favor organice sus clases en jornada diurna o nocturna según su voluntad y ruta asignada")
            with open('profesor_camilo.json', 'r') as archivo:
                profesor_camilo = json.load(archivo)
            with open('profesor_ricardo.json', 'r') as archivo:
                profesor_ricardo = json.load(archivo)
            with open('profesor_jaime.json', 'r') as archivo:
                profesor_jaime = json.load(archivo)

            name = input("\nIngresa tu NOMBRE por favor en minúscula: ")
            # si el nombre es igual a ricardo realiza esto 
            if name == "ricardo":
                studentsbase = {}
                estudiantes_java = []
                estudiantes_node = []
                estudiantes_netcore = []

                # Base de datos para profes; indica salón y estudiantes asignados
                profesor_ricardo = {
                    "java": estudiantes_java,
                    "node.js": estudiantes_node,
                    "netcore": estudiantes_netcore,
                }

                with open('studentsbase.json', 'r') as archivo:
                    studentsbase = json.load(archivo)

                for id, datos in studentsbase.items():
                    if datos["profesores"] == "ricardo-apolo":
                        if datos["rutas"] == "java":
                            estudiantes_java.append(f"{datos['first_name']} {datos['second_name']}, cédula: {id}")
                        elif datos["rutas"] == "node.js":
                            estudiantes_node.append(f"{datos['first_name']} {datos['second_name']}, cédula: {id}")
                        elif datos["rutas"] == "netcore":
                            estudiantes_netcore.append(f"{datos['first_name']} {datos['second_name']}, cédula: {id}")

                print("\nProfesor Ricardo, usted fue asignado el salón APOLO, y sus estudiantes asignados con ruta JAVA son")
                for x in estudiantes_java:
                    print(x)

                print("\nProfesor Ricardo, usted fue asignado el salón APOLO, y sus estudiantes asignados con ruta NODE.JS son")
                for x in estudiantes_node:
                    print(x)

                print("\nProfesor Ricardo, usted fue asignado el salón APOLO, y sus estudiantes asignados con ruta NETCORE son")
                for x in estudiantes_netcore:
                    print(x)

                with open('profesor_ricardo.json', 'w') as archivo:
                    json.dump(profesor_ricardo, archivo)
                    print("Archivo exportado profesor_ricardo")
            # si el nombre es igual a jaime realiza esto 
            elif name == "jaime":
                studentsbase = {}
                estudiantes_java = []
                estudiantes_node = []
                estudiantes_netcore = []
                # base de datos para profes; indica salón y estudiantes asignados
                profesor_Jaime = {
                    "java": estudiantes_java,
                    "node.js": estudiantes_node,
                    "netcore": estudiantes_netcore,
                }

                with open('studentsbase.json', 'r') as archivo:
                    studentsbase = json.load(archivo)

                for id, datos in studentsbase.items():
                    if datos["profesores"] == "jaime-sputnik":
                        if datos["rutas"] == "java":
                            estudiantes_java.append(f"{datos['first_name']} {datos['second_name']}, cédula: {id}")
                        elif datos["rutas"] == "node.js":
                            estudiantes_node.append(f"{datos['first_name']} {datos['second_name']}, cédula: {id}")
                        elif datos["rutas"] == "netcore":
                            estudiantes_netcore.append(f"{datos['first_name']} {datos['second_name']}, cédula: {id}")

                print("\nProfesor Jaime, usted fue asignado el salón APOLO, y sus estudiantes asignados con ruta JAVA son")
                for x in estudiantes_java:
                    print(x)

                print("\nProfesor Jaime, usted fue asignado el salón APOLO, y sus estudiantes asignados con ruta NODE.JS son")
                for x in estudiantes_node:
                    print(x)

                print("\nProfesor Jaime, usted fue asignado el salón APOLO, y sus estudiantes asignados con ruta NETCORE son")
                for x in estudiantes_netcore:
                    print(x)

                with open('profesor_Jaime.json', 'w') as archivo:
                    json.dump(profesor_Jaime, archivo)
                    print("Archivo exportado profesor_Jaime")
            # si el nombre es camilo realiza esto         
            elif name == "camilo":
                studentsbase = {}
                estudiantes_java = []
                estudiantes_node = []
                estudiantes_netcore = []
                # base de datos para profes; indica salón y estudiantes asignados
                profesor_camilo = {
                    "java": estudiantes_java,
                    "node.js": estudiantes_node,
                    "netcore": estudiantes_netcore,
                }

                with open('studentsbase.json', 'r') as archivo:
                    studentsbase = json.load(archivo)

                for id, datos in studentsbase.items():
                    if datos["profesores"] == "camilo-sputnik":
                        if datos["rutas"] == "java":
                            estudiantes_java.append(f"{datos['first_name']} {datos['second_name']}, cédula: {id}")
                        elif datos["rutas"] == "node.js":
                            estudiantes_node.append(f"{datos['first_name']} {datos['second_name']}, cédula: {id}")
                        elif datos["rutas"] == "netcore":
                            estudiantes_netcore.append(f"{datos['first_name']} {datos['second_name']}, cédula: {id}")

                print("\nProfesor Camilo, usted fue asignado el salón APOLO, y sus estudiantes asignados con ruta JAVA son")
                for x in estudiantes_java:
                    print(x)

                print("\nProfesor Camilo, usted fue asignado el salón APOLO, y sus estudiantes asignados con ruta NODE.JS son")
                for x in estudiantes_node:
                    print(x)

                print("\nProfesor Camilo, usted fue asignado el salón APOLO, y sus estudiantes asignados con ruta NETCORE son")
                for x in estudiantes_netcore:
                    print(x)

                with open('profesor_camilo.json', 'w') as archivo:
                    json.dump(profesor_camilo, archivo)
                    print("Archivo exportado profesor_camilo")

        elif saludo == 5:
            estudiantes_java = {}
            estudiantes_netcore = {}
            estudiantes_node = {}
            print("Estos son los estudiantes con Todos sus datos organizados por RUTAS de aprendizaje")
            with open('studentsbase.json', 'r') as archivo:
                studentsbase = json.load(archivo)
            for student_id, datos in studentsbase.items():
                if datos["rutas"] == "java":
                    estudiantes_java[student_id] = datos
                elif datos["rutas"] == "netcore":
                    estudiantes_netcore[student_id] = datos
                elif datos["rutas"] == "node.js":
                    estudiantes_node[student_id] = datos
            print("\n", estudiantes_node)
            print("\n", estudiantes_java)
            print("\n", estudiantes_netcore)
        elif saludo == 6:
            print("¡Este es el historial de notas:")
            with open('active_notasrutas.json', 'r') as archivo:
                active_notasrutas = json.load(archivo)
            
            for id, datos in active_notasrutas.items():
                nota_final = datos.get("Nota_final", "No disponible")
                print(f"{id}: {nota_final}")

        elif saludo == 7:
            print("¡Estos son nuestros graduados! Felicidades, estos estudiantes pasaron.")
            print("Tenemos que ingresar aún más datos")
        
            with open('active_notasrutas.json', 'r') as archivo:
                active_notasrutas = json.load(archivo)
        
            for id, datos in active_notasrutas.items():
                if datos["Nota_final"]>= 60:
                    print(f"{id}: {datos['Nota_final']}")

        elif saludo == 8:
            break

