import psycopg2
from faker import Faker
from os import system
import random

def ejecutar_dummy(username, password, host):
    # Establecer conexión con la base de datos
    conn = psycopg2.connect(
        dbname="hospital",
        user=username,
        password=password,
        host=host
    )

    # Crear un cursor para ejecutar consultas SQL
    cur = conn.cursor()

    fake = Faker('es_ES')

    # Comprobar si existe un registro con id_medico en la tabla ENFERMERA
    def check_id_medico_exist(id_medico):
        cur.execute("SELECT COUNT(*) FROM ENFERMERA WHERE id_medico = %s", (id_medico,))
        count = cur.fetchone()[0]
        return count > 0

    # Generar datos para la tabla PERSONAL
    personal_data = []
    for _ in range(450):
        nombre = fake.first_name()
        apellidos = fake.last_name() + ' ' + fake.last_name()
        dni = fake.unique.random_int(min=10000000, max=99999999)
        personal_data.append((nombre, apellidos, dni))

    # Insertar datos en la tabla PERSONAL
    print("Insertar datos en la tabla PERSONAL...")
    cur.executemany("INSERT INTO PERSONAL (nombre, apellidos, dni) VALUES (%s, %s, %s)", personal_data)
    print("Los datos se han insertado en la tabla PERSONAL.")

    # Generar datos para la tabla MEDICO
    medico_data = []
    for i in range(100):
        id_personal = i + 1  # El identificador de MEDICO coincide con el número de orden
        estudios = 'Medicina'
        especialidad = fake.job()
        curriculum = fake.text(max_nb_chars=200)
        medico_data.append((id_personal, estudios, especialidad, curriculum))

    # Insertar datos en la tabla MEDICO
    print("Insertar datos en la tabla MEDICO...")
    cur.executemany("INSERT INTO MEDICO (id_personal, estudios, especialidad, curriculum) VALUES (%s, %s, %s, %s)", medico_data)
    print("Los datos se han insertado en la tabla MEDICO.")

    # Generar datos para la tabla ENFERMERA
    enfermera_data = []
    for i in range(100, 300):  # Comenzar desde 100 para evitar repetir id_personal de MEDICO
        id_personal = i + 1  # El identificador de ENFERMERA coincide con el número de orden
        anos_de_experiencia = fake.random_int(min=1, max=20)
        id_medico = random.randint(1, 100) if i % 2 != 0 else None  # Cada segundo ENFERMERA tendrá una referencia a MEDICO
        enfermera_data.append((id_personal, anos_de_experiencia, id_medico))

    # Insertar datos en la tabla ENFERMERA con comprobación de existencia de id_medico
    print("Insertar datos en la tabla ENFERMERA...")
    for data in enfermera_data:
        id_medico = data[2]
        if id_medico is None or not check_id_medico_exist(id_medico):
            cur.execute("INSERT INTO ENFERMERA (id_personal, anos_de_experiencia, id_medico) VALUES (%s, %s, %s)", data)
    print("Los datos se han insertado en la tabla ENFERMERA.")

    # Generar datos para la tabla VARIO
    vario_data = []
    for i in range(300, 400):  # Comenzar desde 300 para evitar repetir id_personal de MEDICO y ENFERMERA
        id_personal = i + 1  # El identificador de VARIO coincide con el número de orden
        tipo = 'Neteja'  # Se especifica el tipo 'Neteja', como se requiere
        vario_data.append((id_personal, tipo))

    # Insertar datos en la tabla VARIO
    print("Insertar datos en la tabla VARIO...")
    cur.executemany("INSERT INTO VARIO (id_personal, tipo) VALUES (%s, %s)", vario_data)
    print("Los datos se han insertado en la tabla VARIO.")

    # Generar datos para la tabla PACIENTE
    paciente_data = []
    for _ in range(10000):
        dni_letters = fake.random_element(elements=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'))
        dni_numbers = fake.random_number(digits=8)
        dni = f"{dni_numbers}{dni_letters}"
        nombre = fake.first_name()
        apellidos = fake.last_name() + ' ' + fake.last_name()
        paciente_data.append((dni, nombre, apellidos))

    # Insertar datos en la tabla PACIENTE
    print("Insertar datos en la tabla PACIENTE...")
    cur.executemany("INSERT INTO PACIENTE (dni_paciente, nombre, apellidos) VALUES (%s, %s, %s)", paciente_data)
    print("Los datos se han insertado en la tabla PACIENTE.")

    # Generar datos para la tabla RES_VIS
    res_vis_data = []
    for _ in range(100000):
        dni_paciente = random.choice(paciente_data)[0]  # Generar un dni de paciente aleatorio de los existentes
        id_personal = random.randint(1, 450)  # Generar un id de personal aleatorio
        res_vis_data.append((id_personal, dni_paciente))

    # Insertar datos en la tabla RES_VIS
    print("Insertar datos en la tabla RES_VIS...")
    cur.executemany("INSERT INTO RES_VIS (id_personal, dni_paciente) VALUES (%s, %s)", res_vis_data)
    print("Los datos se han insertado en la tabla RES_VIS.")

    # Confirmar todas las operaciones y cerrar cursor y conexión
    conn.commit()
    cur.close()
    conn.close()
    system("cls")
    print("-"*30)
    print("Todas las operaciones se han completado. La conexión con la base de datos se ha cerrado.")
    print("-"*30)
