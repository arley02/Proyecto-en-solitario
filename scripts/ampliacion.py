import psycopg2
from psycopg2 import Error
from os import system

def historial_paciente(username, password, host):
    try:
        # Conexión a la base de datos
        connection = psycopg2.connect(host=host, dbname="hospital", user=username, password=password)

        cursor = connection.cursor()

        system("cls")
        # Pedir el DNI del paciente al usuario
        dni_paciente = input("Ingrese el DNI del paciente para ver su historial médico: ")

        # Consulta SQL para obtener el historial médico del paciente
        consulta_sql = """
        SELECT
            P.dni_paciente,
            P.nombre,
            P.apellidos,
            H.fecha,
            D.nombre_diagnostico,
            D.descripcion AS descripcion_diagnostico,
            D.tratamiento AS tratamiento_diagnostico,
            H.medicamentos_recibidos,
            HV.id_habitacion,
            QV.id_quirofano,
            E.nombre_equipo AS equipo_usado,
            E.marca AS marca_equipo,
            E.modelo AS modelo_equipo
        FROM
            PACIENTE P
            JOIN RES_VIS V ON P.dni_paciente = V.dni_paciente
            JOIN HISTORIAL_MEDICO H ON V.id_visita = H.id_visita
            LEFT JOIN DIAGNOSTICO D ON H.codigo_diagnostico = D.codigo_diagnostico
            LEFT JOIN HABITACION_VISITADA HV ON V.id_visita = HV.id_visita
            LEFT JOIN QUIROFANO_VISITADA QV ON V.id_visita = QV.id_visita
            LEFT JOIN EQUIPA E ON 
                (HV.id_habitacion IS NOT NULL AND CAST(HV.id_habitacion AS INTEGER) = E.id_equipamiento) OR 
                (QV.id_quirofano IS NOT NULL AND QV.id_quirofano = CAST(E.id_equipamiento AS VARCHAR))
        WHERE
            P.dni_paciente = %s
        ORDER BY
            H.fecha;
        """

        # Ejecutar la consulta SQL
        cursor.execute(consulta_sql, (dni_paciente,))
        historial = cursor.fetchall()

        if len(historial) == 0:
            print("No se encontraron registros para el paciente con ese DNI.")
        else:
            # Mostrar el historial médico del paciente
            print("\nHistorial médico del paciente:")
            for visita in historial:
                print(f"DNI: {visita[0]}\nNombre: {visita[1]}\nApellidos: {visita[2]}\nFecha: {visita[3]}\nDiagnóstico: {visita[4]}\nDescripción Diagnóstico: {visita[5]}\nTratamiento Diagnóstico: {visita[6]}\nMedicamentos Recibidos: {visita[7]}\nHabitación: {visita[8]}\nQuirófano: {visita[9]}\nEquipo Usado: {visita[10]}\nMarca: {visita[11]}\nModelo: {visita[12]}\n")
            
            input("\nPresione Enter para continuar...")
            system("cls") 
    except (Exception, Error) as error:
        print("Error al acceder a la base de datos:", error)

    finally:
        # Cerrar la conexión a la base de datos
        if connection:
            cursor.close()
            connection.close()
            print("Conexión cerrada.")

