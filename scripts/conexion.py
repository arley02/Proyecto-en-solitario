import psycopg2
from psycopg2 import OperationalError
from os import system
from consultas_i_informes import *
from Dummy import ejecutar_dummy
from eliminar_dummy import verificar_eliminar
from mantenimiento import mantenimiento
from ampliacion import historial_paciente

def login(credenciales):
    # Pedir usuario y contraseña para la conexión
    username = input("Introduïu el nom d'usuari: ")
    password = input("Introduïu la contrasenya: ")
    system("cls")
    hosts = ["192.168.56.112", "192.168.56.123"]
    connected = False
    
    for host in hosts:
        if connected:
            break
        try:
            conn = psycopg2.connect(host=host, dbname="hospital", user=username, password=password)
            connected = True
            print("-" * 20)
            print(host)
            print("-" * 20)
            x = " "
            while x != "7":
                print("Menu Gestio Hospital")
                print("-" * 20)
                print("\n 1 . Manteniments\n 2 . Consultes i informes\n 3 . Exportacio de dades\n 4 . Executar prova de dades\n 5 . Eliminar dades \n 6 . ver historial de un paciente \n 7. salir\n\n")
                x = input("Entra una opcio: ")
                if x == "1":
                    system("cls")
                    mantenimiento(conn)
                elif x == "2":
                    system("cls")
                    menu_consultas(username, password, host)
                elif x == "3":
                    pass
                elif x == "4":
                    ejecutar_dummy(username, password, host)
                elif x == "5":
                    verificar_eliminar(username, password, host)
                elif x == "6":
                    historial_paciente(username, password, host)
                elif x == "7":
                    system("cls")
                    print("-" * 20)
                    print("session cerrada")
                    print("-" * 20)
                    conn.close()
        except OperationalError as e:
            print("-" * 20)
            print(f"Error al conectar al servidor PostgreSQL ({host}): {e}")
            print("-" * 20)
            print("Explorando alternativas de servidor...")
    
    if not connected:
        print("No se pudo conectar a ningún servidor.")

# Registro del usuario, falta configurar para asignar los roles
def registre(new_user, new_password):
    creacio_usuari = f"CREATE USER {new_user} WITH PASSWORD '{new_password}';"
    try:
        # Conexión con el host especificado
        connexio = psycopg2.connect(host="192.168.56.112", user="postgres", password="Blanes2121")
        cur = connexio.cursor()
        cur.execute(creacio_usuari)
        connexio.commit()

        cur.close()
        connexio.close()
    except Exception as e:
        print("Error en intentar crear l'usuari:", e)
