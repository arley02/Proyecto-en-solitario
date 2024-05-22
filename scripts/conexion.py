import psycopg2
from psycopg2 import OperationalError
from os import system
from consultas_i_informes import *
from Dummy import ejecutar_dummy


def login(credenciales):
    # Pedir usuario y contraseña para la conexión
    username = input("Introduïu el nom d'usuari: ")
    password = input("Introduïu la contrasenya: ")
    system("cls")
    # Lista hosts insti
    hosts = ["10.94.254.116", "10.94.255.2"]
    for host in hosts:
        try:
            # Intentar la conexión con el host actual
            conn = psycopg2.connect(host=host, dbname="hospital", user=username, password=password)
            x = " "
            while x != "4":
                print("-"*20)
                print("Menu Gestio Hospital")
                print("-"*20)
                print("\n 1 . Manteniments\n 2 . Consultes i informes\n 3 . Exportacio de dades\n 4 . Executar prova de dades\n 5 . Eliminar dades \n 6 . Sortir\n\n")
                x = input("Entra una opcio: ")
                if x == "1":
                    pass
                elif x == "2":
                    system("cls")
                    menu_consultas(username, password, host)
                elif x == "3":
                    pass
                elif x == "4":
                    ejecutar_dummy(username, password, host)
                elif x == "5":
                    pass
                elif x == "6":
                    system("cls")
                    print("-"*20)
                    print("session cerrada")
                    print("-"*20)
            conn.close()
#            break  # Si la conexión es exitosa, salir del bucle de hosts
        except OperationalError as e:
            # Si hay un error al conectarse, imprime un mensaje indicando el error y prueba con el siguiente host
            print("-"*20)
            print(f"Error al conectar al servidor PostgreSQL ({host}): {e}")
            print("-"*20)
            print("Explorando alternativas de servidor...")

# Registro del usuario, falta configurar para asignar los roles
def registre(new_user, new_password):
    creacio_usuari = f"CREATE USER {new_user} WITH PASSWORD '{new_password}';"
    try:
        # Conexión con el host especificado
        connexio = psycopg2.connect(host="10.94.254.116", user="postgres", password="Blanes2121")
        cur = connexio.cursor()
        cur.execute(creacio_usuari)
        connexio.commit()

        cur.close()
        connexio.close()
    except Exception as e:
        print("Error en intentar crear l'usuari:", e)
