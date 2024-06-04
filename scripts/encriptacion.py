import bcrypt
import csv
from os import system
from cryptography.fernet import Fernet
import base64

# Funció per crear una contrasenya xifrada
def encriptar(password):
    # Generar una clave de encriptación
    clave = b'TuClaveFijaAqui'
    texto_encriptado = base64.b64encode(clave)
    return texto_encriptado

# Carrega de noms d'usuari i contrasenyes d'un fitxer Excel
def cargar_credenciales(file_path):
    credenciales = {}
    with open(file_path, 'r') as File:
        reader = csv.reader(File, delimiter=',')    
        for fila in reader:
            nombre_usuario, contraseña = fila
            credenciales[nombre_usuario] = contraseña
    return credenciales

# Afegir un nou compte
def datos_encript(file_path, username, password):
    datos = [username, encriptar(password)]
    with open(file_path, 'a',newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(datos)
# Accedir al sistemax

# Ruta al fitxer Excel amb noms d'usuari i contrasenyes
#-----------------------------------cal crear el fitxer credentials.xlsx i modificar la ruta----------------------------
file_path = "PROG/credenciales.csv"

