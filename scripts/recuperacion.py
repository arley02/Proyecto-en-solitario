import os
import subprocess
from datetime import datetime
import gzip
import shutil

# Configuraciones
PG_USER = "postgres"
PG_PASSWORD = "Blanes2121"
PG_HOST = "localhost"
BACKUP_PATH = "/etc/postgresql/15/main/backups/backups_logicos"
LOG_FILE = "/etc/postgresql/15/main/logs_backups/backup.log"

def log_message(message):
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def restore_logico():
    DB = "hospital"
    file_date = datetime.now().strftime('%Y%m%d')
    file_sql = f"{BACKUP_PATH}/{DB}-{file_date}.sql"
    backup_file_gz = f"{BACKUP_PATH}/{DB}-{file_date}.sql.gz"

    try:
        # Descomprimir el archivo de backup
        with gzip.open(backup_file_gz, 'rb') as f_in:
            with open(file_sql, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        log_message(f"Descompresión de {backup_file_gz} completada")

        # Restaurar la base de datos
        restore_command = [
            'psql',
            '-h', PG_HOST,
            '-U', PG_USER,
            '-d', DB,
            '-f', file_sql
        ]

        result = subprocess.run(
            restore_command,
            env={'PGPASSWORD': PG_PASSWORD},
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            log_message(f"Restauración lógica de {DB} completada correctamente")
        else:
            log_message(f"ERROR: Restauración lógica de {DB} fallida\n{result.stderr}")

    except Exception as e:
        log_message(f"ERROR: Fallo durante la restauración de {DB} - {str(e)}")

    finally:
        # Eliminar el archivo temporal descomprimido si existe
        if os.path.exists(file_sql):
            os.remove(file_sql)
            log_message(f"Archivo temporal {file_sql} eliminado")

if __name__ == "__main__":
    restore_logico()
