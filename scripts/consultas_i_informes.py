import psycopg2
from os import system

def menu_consultas(username, password, host):
    conn = psycopg2.connect(host=host, dbname="hospital", user=username, password=password)
    x = " "
    while x != "4":
        print("-" * 20)
        print("Menu de consultes i informes")
        print("-" * 20)
        print("\n 1 . Consultas de les plantes\n 2 . Informe de personal\n 3 . Informe de nombre de visites per dia\n 4 . Sortir\n\n")
        x = input("Entra una opcio: ")

        if x == "1":
            system("cls")
            continuar = "si"
            while continuar.lower() == "si":
                numero_planta = input("Numero de planta: ")
                try:
                    cur = conn.cursor()
                    cur.execute("""
                        SELECT 
                            COUNT(DISTINCT h.numero_habitacion) AS num_habitaciones,
                            COUNT(DISTINCT q.id_quirofano) AS num_quirofanos,
                            COUNT(DISTINCT e.id_enfermera) AS num_enfermeras
                        FROM 
                            planta p
                        LEFT JOIN 
                            habitacion h ON p.numero_planta = h.numero_planta
                        LEFT JOIN 
                            quirofano q ON p.numero_planta = q.numero_planta
                        LEFT JOIN 
                            enfermera e ON p.numero_planta = e.numero_planta
                        WHERE 
                            p.numero_planta = %s
                    """, (numero_planta,))
            
                    resultado = cur.fetchone()
                    print("-"*20)
                    print("Planta:", numero_planta)
                    print("Número de habitaciones:", resultado[0])
                    print("Número de quirófanos:", resultado[1])
                    print("Número de enfermeras:", resultado[2])
                    print("-"*20)
                    #PONER UN BLUCLE PARA PREGUNTAR SI DESEA CONTINUAR
                    continuar = input("¿Desea continuar? (si/no): ").lower()
                    system("cls")
                    while continuar not in ["si", "no"]:
                        print("Opción incorrecta, por favor ingrese 'si' o 'no'")
                        continuar = input("¿Desea continuar? (si/no): ").lower()
                        system("cls")                   
                except psycopg2.Error as e:
                    print("Error al ejecutar la consulta:", )

                finally:
                    cur.close()

        elif x == "2":
            system("cls")
            continuar = "no"
            while continuar.lower() == "no":
                try:
                    cur = conn.cursor()
                    cur.execute("""
                        SELECT p.nombre, p.apellidos, 
                            CASE WHEN m.id_medico IS NOT NULL THEN 'Médico'
                                    WHEN e.id_enfermera IS NOT NULL THEN 'Enfermera'
                                    WHEN v.id_visita IS NOT NULL THEN 'Personal Visitante'
                                    ELSE 'Otro Personal'
                            END AS tipo_personal
                        FROM personal p
                        LEFT JOIN medico m ON p.id_personal = m.id_personal
                        LEFT JOIN enfermera e ON p.id_personal = e.id_personal
                        LEFT JOIN res_vis v ON p.id_personal = v.id_personal
                    """)
        
                    resultados = cur.fetchall()
                    # Encabezados
                    print("Informe de Personal del Hospital:")
                    print("{:<20} {:<20} {:<20}".format("Nombre", "Apellidos", "Tipo de Personal"))
                    print("-" * 60)

                    for resultado in resultados:
                        nombre = resultado[0]
                        apellidos = resultado[1]
                        tipo_personal = resultado[2]
                        print("{:<20} {:<20} {:<20}".format(nombre, apellidos, tipo_personal))
                        #PONER UN BLUCLE PARA PREGUNTAR SI DESEA CONTINUAR
                    continuar = input("¿Desea salir? (si/no): ").lower()
                    system("cls")
                    while continuar not in ["si", "no"]:
                        print("Opción incorrecta, por favor ingrese 'si' o 'no'")
                        continuar = input("¿Desea salir? (si/no): ").lower()
                        system("cls") 
                except psycopg2.Error as e:
                    print("Error al ejecutar la consulta:", e)

                finally:
                    # Cerrar el cursor y la conexión
                    cur.close()

        elif x == "3":
            system("cls")
            try:
                cur = conn.cursor()
                cur.execute('''SELECT
                        hm.fecha,
                        COUNT(rv.id_visita) AS numero_visitas,
                        p.nombre AS nombre_paciente,
                        pe.nombre AS nombre_medico,
                        pe.apellidos AS apellidos_medico
                    FROM 
                        historial_medico hm
                    JOIN 
                        res_vis rv ON hm.id_visita = rv.id_visita
                    JOIN 
                        paciente p ON rv.dni_paciente = p.dni_paciente
                    JOIN 
                        medico m ON hm.id_personal_doctor = m.id_personal
                    JOIN
                        personal pe ON m.id_personal = pe.id_personal
                    GROUP BY 
                        hm.fecha, nombre_paciente, apellidos_medico, nombre_medico
                    ORDER BY 
                        hm.fecha;''')
                
                results = cur.fetchall()

                        # Imprimir los resultados
                print("{:<15} | {:<20} | {:<30} | {}".format("Fecha", "Número de Visitas", "Médico", "Paciente"))
                print("-"*80)
                for row in results:
                    print("{:<15} | {:<20} | {:<30} | {}".format(row[0], row[1], f"{row[3]} {row[4]}", row[2]))
                
                input("\nIntroduzca cualquier caracter para continuar: ")
                system("cls") 
            except psycopg2.Error as e:
                print("Error al ejecutar la consulta:", e)

            finally:
                # Cerrar el cursor y la conexión
                cur.close()
                     
        elif x == "4":
            x = "4"
            conn.close() 
            system("cls")

        elif x == str:
            print("--por favor Seleccione una opcion valida-- ")
            system("cls")

    conn.close()
