import psycopg2
from os import system

def dar_alta_personal(conn):
    nombre = input("Ingrese el nombre del nuevo personal: ")
    rol = input("Ingrese el rol del nuevo personal (Médico, Enfermera, Administrativo, Limpieza): ")

    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO PERSONAL (nombre, apellidos, dni) VALUES (%s, %s, %s) RETURNING id_personal;",
                           (nombre, "Apellido", "DNI123"))
            id_personal = cursor.fetchone()[0]

            if rol.lower() == "médico":
                cursor.execute("INSERT INTO MEDICO (id_personal, estudios, especialidad, curriculum) VALUES (%s, %s, %s, %s);",
                               (id_personal, "Estudios", "Especialidad", "Curriculum"))
            elif rol.lower() == "enfermera":
                cursor.execute("INSERT INTO ENFERMERA (id_personal, anos_de_experiencia) VALUES (%s, %s);",
                               (id_personal, 0))
            else:
                cursor.execute("INSERT INTO VARIO (id_personal, tipo) VALUES (%s, %s);", (id_personal, rol))

            conn.commit()
            print(f"{rol} {nombre} dado de alta exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al dar de alta al nuevo personal: {e}")

def dar_alta_paciente(conn):
    dni = input("Ingrese el DNI del paciente: ")
    nombre = input("Ingrese el nombre del paciente: ")
    apellidos = input("Ingrese los apellidos del paciente: ")

    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO PACIENTE (dni_paciente, nombre, apellidos, estado) VALUES (%s, %s, %s, %s);",
                           (dni, nombre, apellidos, 'alta'))
            conn.commit()
            print(f"Paciente {nombre} dado de alta exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al dar de alta al nuevo paciente: {e}")

def verificar_dependencia(conn):
    try:
        with conn.cursor() as cursor:
            query = """
                SELECT 
                    id_enfermera,
                    CASE 
                        WHEN id_medico IS NOT NULL THEN 'Depende de un médico/SSA'
                        WHEN numero_planta IS NOT NULL THEN 'Pertenece a una planta'
                        ELSE 'No se pudo determinar la dependencia'
                    END AS dependencia
                FROM ENFERMERA;
            """
            cursor.execute(query)
            dependencias = cursor.fetchall()
            print("Dependencias del personal de enfermería:")
            for id_enfermera, dependencia in dependencias:
                print(f"ID Enfermera: {id_enfermera}, Dependencia: {dependencia}")
            input("\nIntroduzca cualquier caracter para continuar: ")
            system("cls") 
    except psycopg2.Error as e:
        print("Error al verificar la dependencia del personal de enfermería:", e)

def operaciones_previstas(conn):
    fecha = input("Ingrese la fecha (YYYY-MM-DD) para la que desea ver las operaciones previstas: ")

    try:
        with conn.cursor() as cursor:
            query = """
                SELECT 
                    q.numero_quirofan, 
                    o.hora, 
                    p.nombre AS paciente, 
                    m.nombre AS medico, 
                    e.nombre AS enfermera
                FROM 
                    OPERACION o
                JOIN 
                    QUIROFANO q ON o.id_quirofano = q.id_quirofano
                JOIN 
                    PACIENTE p ON o.dni_paciente = p.dni_paciente
                JOIN 
                    MEDICO m ON o.id_medico = m.id_medico
                LEFT JOIN 
                    ENFERMERA e ON o.id_enfermera = e.id_enfermera
                WHERE 
                    o.fecha = %s;
            """
            cursor.execute(query, (fecha,))
            operaciones = cursor.fetchall()
            print(f"Operaciones previstas para el día {fecha}:")
            for numero_quirofan, hora, paciente, medico, enfermera in operaciones:
                print(f"Quirófano: {numero_quirofan}, Hora: {hora}, Paciente: {paciente}, Médico: {medico}, Enfermera: {enfermera if enfermera else 'No asignada'}")
            input("\nIntroduzca cualquier caracter para continuar: ")
            system("cls")
    except psycopg2.Error as e:
        print(f"Error al obtener las operaciones previstas: {e}")

def visitas_planificadas(conn):
    fecha = input("Ingrese la fecha (YYYY-MM-DD) para la que desea ver las visitas planificadas: ")

    try:
        with conn.cursor() as cursor:
            query = """
                SELECT 
                    v.hora_entrada, 
                    p.nombre AS paciente, 
                    m.nombre AS medico
                FROM 
                    VISITA v
                JOIN 
                    PACIENTE p ON v.dni_paciente = p.dni_paciente
                JOIN 
                    MEDICO m ON v.id_medico = m.id_medico
                WHERE 
                    v.fecha = %s;
            """
            cursor.execute(query, (fecha,))
            visitas = cursor.fetchall()
            print(f"Visitas planificadas para el día {fecha}:")
            for hora_entrada, paciente, medico in visitas:
                print(f"Hora de entrada: {hora_entrada}, Paciente: {paciente}, Médico: {medico}")
            input("\nIntroduzca cualquier caracter para continuar: ")
            system("cls")
    except psycopg2.Error as e:
        print(f"Error al obtener las visitas planificadas: {e}")

def mantenimiento(conn):
    while True:
        print("-" * 30)
        print("Menú de Mantenimiento")
        print("-" * 30)

        print("\n 1. Dar de alta a nuevo personal del centro")
        print("2. Dar de alta a un paciente nuevo")
        print("3. Verificar dependencia del personal de enfermería")
        print("4. Ver operaciones previstas")
        print("5. Ver visitas planificadas")
        print("6. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                dar_alta_personal(conn)
            elif opcion == 2:
                dar_alta_paciente(conn)
            elif opcion == 3:
                verificar_dependencia(conn)
            elif opcion == 4:
                operaciones_previstas(conn)
            elif opcion == 5:
                visitas_planificadas(conn)
            elif opcion == 6:
                print("Saliendo del menú de mantenimiento...")
                system("cls")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero.")
