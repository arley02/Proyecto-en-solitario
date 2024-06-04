## SOLUCION DE ERROR DE REPLICACION

si el adaptador en ambas maquinas es adaptador puente al cambiar de red la replicacion "fallara", para solucionarlo hacer el siguiente procedimiento:

1. para la el servicio postgresql del servidor secundario "sudo systemctl stop postgresql"
2. eliminar el contenido con la siguiente comanda en la siguiente ruta:

   ![1716393058503](image/Readme/1716393058503.png)
3. en el servidor principal eliminar la replica en psql

   ![1716397600748](image/Readme/1716397600748.png)

   en este caso la replica se llama replica_1
4. despues conectarse al nodo principal (servidor principal) con la siguiente comanda:

   ![1716397658613](image/Readme/1716397658613.png)
5. una vez hecho hacemos la siguiente comanda:

   ![1716397743659](image/Readme/1716397743659.png)

   una vez el servicio postgres iniciado lo comprovamos.
6. 

## [Para más informacion de revise el markdown &#34;documento final de insta&#34;](https://github.com/arley02/Treball_Projecte/blob/main/PROJECTO%20PROG%20I%20BD%20.md#esquema-de-seguridad)

revisar el panel para ver en menu:

![1717538523200](image/Readme/1717538523200.png)
