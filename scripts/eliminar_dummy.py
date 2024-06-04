import psycopg2
import random
from faker import Faker
from os import system

def eliminar_datos(username, password, host):
    # Conexión
    conn = psycopg2.connect(
        dbname="hospital",
        user=username,
        password=password,
        host=host
    )
    cur = conn.cursor()


# Función para eliminar todos los datos insertados

    try:
        cur.execute("DELETE FROM vario")
        print("Datos de la tabla vario eliminados.")

        cur.execute("DELETE FROM res_vis")
        print("Datos de la tabla res_vis eliminados.")

        cur.execute("DELETE FROM enfermera")
        print("Datos de la tabla enfermera eliminados.")

        cur.execute("DELETE FROM medico")
        print("Datos de la tabla medico eliminados.")

        cur.execute("DELETE FROM PERSONAL")
        print("Datos de la tabla PERSONAL eliminados.")

        cur.execute("DELETE FROM PACIENTE")
        print("Datos de la tabla PACIENTE eliminados.")
        
        conn.commit()
        system("cls")
        print("-"*30)
        print("Todos los datos insertados han sido eliminados.")
        print("-"*30)
    except Exception as e:
        print(f"Error al eliminar datos: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def verificar_eliminar(username, password, host):
    delete_confirmation = input("¿Desea eliminar todos los datos insertados? (s/n): ")
    if delete_confirmation.lower() == 's':
        eliminar_datos(username, password, host)
    else:
        print("Los datos han sido conservados en la base de datos.")