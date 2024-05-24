# **Matriz de usuarios**

|           ROLES           |                PERMISOS                | TABLAS AFECTADAS                                                                                                                |
| :------------------------: | :------------------------------------: | ------------------------------------------------------------------------------------------------------------------------------- |
|          Medicos          |   SELECT - INSERT - UPDATE - DELETE   | HISTORIAL_MEDICO, DIAGNOSTICO, RES/VIS                                                                                          |
|          Medicos          |                 SELECT                 | EQUIPAMIENTO, HABITACION, PLANTA, QUIROFANO                                                                                     |
|         Enfermeras         |                 SELECT                 | PACIENTE, HISTORIAL_MEDICO, DISAGNOSTICO, RES/VIS, HABITACION_VISTIDA, QUIROFANO_VISITADO, QUIROFANO, HABITACION, EQUIPAMIENTOS |
|         Recepcion         |                 SELECT                 | RES/VIS, HABITACION_VISITADA, HABITACION                                                                                        |
|         logopedas         |                 SELECT                 | PACIENTE, HISTORIAL_MEDICO, DIAGNOSTICO, RES/VIS                                                                                |
|      fisioterapeutas      |                 SELECT                 | PACIENTE, HISTORIAL_MEDICO, DIAGNOSTICO, RES/VIS, HABITACION                                                                    |
| Administrador informatico | todos los permisos de todas las tablas | todas las tablas del esquema                                                                                                    |
| Administrador del hospital |           todos los permisos           | PERSONAL, EQUIPAMIENTO                                                                                                          |
|  Conductor de ambulancia  |             SELECT- INSERT             | RES/VIS                                                                                                                         |

---

## Medicos

el personal Medico en las tablas HISTORIAL_MEDICO, DIAGNOSTICO, RES/VIS pueden hacer SELECT, INSERT, UPDATE, DELETE pero en la tablas EQUIPAMIENTO, HABITACION, PLANTA, QUIROFANO, solo tendran permiso de SELECT.

## Enfermeras

El personal de enfermeras deben poder hacer un SELECT en las siguientes tablas: PACIENTE, HISTORIAL_MEDICO, DIAGNOSTICO, RES/VIS, HABITACION_VISTIDA, QUIROFANO_VISITADO, QUIROFANO, HABITACION, EQUIPAMIENTOS

## Recepcionista

Recepcion tendra permisos de SELECT en las siguientes tablas: RES/VIS, HABITACION_VISITADA, HABITACION.

## Logopedas

los logopedas deben poder hacer un SELECT en las siguientes tablas: PACIENTE, HISTORIAL_MEDICO, DIAGNOSTICO, RES/VIS.

## Fisioterapeutas

los logopedas deben poder hacer un SELECT en las siguientes tablas: PACIENTE, HISTORIAL_MEDICO, DIAGNOSTICO, RES/VIS, HABITACION.

## Administrador informatico

los administradores de informatica deben tener todos los permisos sobre todas las tablas.

## Administrador del hospital

el adminsitrador del hospital tiene todos los permisos sobre la tabla de PERSONAL, EQUIPAMIENTO

## Conductor de ambulancia

el conductor o auxiliar de ambulancia deben poder hacer un SELECT, INSERT en la tabla RES/VIS esto para informar el estado o hora de entrada de paciente.
