import bcrypt
from os import system
from encriptacion import *
from conexion import *

x = " "
while x != "0":

    # Selección del modo: iniciar sesión o crear una nueva cuenta
    mode = input("Seleccione el modo:\n 1 - Iniciar sesión\n 2 - Crear una cuenta\n 0 - Salir \n \n  Seleccione una opción: ")

    if mode == "1":
        credenciales = cargar_credenciales(file_path)
        system("cls")
        login(credenciales)
    elif mode == "2":
        credenciales = cargar_credenciales(file_path)
        system("cls")
        new_username = input("Introduzca el nuevo nombre de usuario: ")
        new_password = input("Introduzca la nueva contraseña: ")
        system("cls")
        # comprobación si el usuario ya está creado
        if new_username in credenciales:
            print("-"*20)
            print("| ¡El usuario ya existe! |")
            print("-"*20)
        else:
            datos_encript(file_path, new_username, new_password)
            registre(new_username, new_password)
            system("cls")
            print("-"*30)
            print("| ¡La cuenta se ha creado con éxito! | ")
            print("-"*30)

    elif mode == "0":
        system("cls")
        print("Saliendo del sistema")
        x = "0"
    else:
        system("cls")
        print("Modo incorrecto. Por favor, seleccione 1 o 2.")
