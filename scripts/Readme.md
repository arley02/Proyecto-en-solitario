# USO DE EJECUCION SCRIPT

en caso de descargar los ficheros verificar que todos se encuentran en el misma carpeta tambien los usuarios tiene que verificar que el fichero "credenciales" tambien esta creada.

para ejecutar el script es importante ejecutar solo el script "main_login.py"

![1716236752793](imagenes_scripts/1716236752793.png)

### importante!!!

en el script "conexion.py" debemos cambiar las ips que se conectan al servidor:

![1716237250483](imagenes_scripts/1716237250483.png)

donde pone host cambiamos las ips por las ips de los servidores donde se encuentra alojado la base de datos, en este caso hay dos por que la primera ip es la del servidor principal (NODO 1) y la segunda seria el servidor secundario (NODO 2) diseñado para que en caso que una falle la otra siga ofreciendo conexion.


## LOGIN

Los usuario tendran 3 opciones iniciar sesion, registrarse en caso de no tener un usuario o salir del programa.

![1717531180639](image/Readme/1717531180639.png)

cuando el usuario inicie sesion y la cuenta exista verificara que tipo de rol tiene y este tedra ciertas opciones.

#### IMPORTANTE!!

se a rediseñado para que por ejemplo los usuarios con roles para que determinados usuarios puedan ejecutar ciertas opciones por ejemplo:

administrador informatico: dar de alta a nuevo personal entre otras opciones como consultas (mantenimiento y consultas).

administador del hospital podra dar de alta a nuevos pacientes tambien puede dar de alta a nuevo personal entre otras opciones (mantenimiento y consultas.

el resto de roles tendran mas o menos opciones y el personal como medicos o enfermeras podran hacer consultas.
