# **Matriz de usuarios**

## Medicos

el personal Medico en las tablas HISTORIAL_MEDICO, Diagnostico, RES/VIS pueden hacer SELECT, INSERT, UPDATE, DELETE pero en la tablas EQUIPAMIENTO, HABITACION, PLANTA, QUIROFANO, solo tendran permiso de SELECT.

## Enfermeras

El personal de enfermeras debe poder hacer un SELECT en las suguientes tablas: PACIENTE, HISTORIAL_MEDICO, DISAGNOSTICO, RES/VIS, HABITACION_VISTIDA, QUIROFANO_VISITADO, QUIROFANO, HABITACION, EQUIPAMIENTOS

|   ROLES   | PERMISOS                            |
| :--------: | ----------------------------------- |
|  Medicos  | SELECT - INSERT - UPDATE - DELETE - |
| Enfermeras |                                     |

---
