# ENUNCIADO DE LA BASE DE DATOS

## En calatan:

Per portar part de la gestió de l’hospital de Blanes sabem que :

* En l’hospital hi treballa personal mèdic (metges/metgesses), personal d’infermeria i personal vari (zeladors, administratius, conductors d’ambulàncies, etc. ). Dels personal mèdic ens interessarà guardar gran quantitat de informació referent als seus estudis, currículum, etc. La informació específica a guardar del personal d’infermeria serà diferent, però també caldrà guardar molta informació. Del personal vari solament ens interessen les seves dades personals i un atribut “tipus feina”.
* Cada membre del personal mèdic té una única especialitat i té assignades una o més persones d’infermeria. Els membres del personal d’infermeria están assignat a un únic metge/ssa o bé, són de planta d’hospital que no estan assignades a cap metge/ssa en particular.
* L’hospital està format per quatre plantes que les identifiquem amb el número de planta (primera, segona, tercera i quarta). A cada planta hi ha diferents habitacions i també pot haver-hi quiròfans. Els quiròfans disposen d’una gran quantitat d’aparells mèdics (respiradors, màquines d’oxigen, etc.). Cada aparell mèdic està assignat a un únic quiròfan i es vol saber quants en hi ha de cada un d’ells a cada quiròfan. Dins de cada planta els quiròfans ens venen identificat per número de quiròfan, el Q1, el Q2 ... i així successivament.
* Els pacients, d’entrada són atesos en una visita realitzada per un metge/ssa. Es possible que en visites posteriors aquest pacients siguin visitats per un altre metge/ssa. Per cada visita caldrà guardar el diagnòstic, així com els medicaments que li ha receptat, si és el cas.
* Es vol portar un control de les visites que els malalts fan a cada metge/ssa. Per això i per cada dia i per cada metge/ssa caldrà saber l’hora de visita de cada un dels seus pacients.
* També es vol portar un control de les reserves d’habitacions dels pacients que cal ingressar. Per això i per cada una de les habitacions es vol saber les reserves que té, és a dir dia previst de ingrés, dia previst de sortida i de quin pacient es tracta.
* Finalment es vol portar un control de cada un dels quiròfans i de les reserves previstes per fer-hi operacions. Per això i per a cada un dels quiròfans, es vol saber per cada dia i hora el metge que el té reservat i el pacient a qui s’operarà. No tots els pacients que són ingressats cal operar-los. Considereu que cada operació la fa un sol metge i que és assistit per varis membres del personal d’infermeria.

## En español

Para llevar parte de la gestión del hospital de Blanes sabemos que:

- En el hospital trabaja personal médico (médicos/médicas), personal de enfermería y personal vario (celadores, administrativos, conductores de ambulancias, etc.). De los personal médico nos interesará guardar gran cantidad de información referente a sus estudios, currículum, etc. La información específica a guardar del personal de enfermería será diferente, pero también será necesario guardar mucha información. Del personal vario sólo nos interesan sus datos personales y un atributo “tipo trabajo”.
- Cada miembro del personal médico tiene una única especialidad y tiene asignadas una o más personas de enfermería. Los miembros del personal de enfermería están asignados a un único médico o bien, son de planta de hospital que no están asignadas a ningún médico en particular.
- El hospital está formado por cuatro plantas que las identificamos con el número de planta (primera, segunda, tercera y cuarta). En cada planta hay diferentes habitaciones y también puede haber quirófanos. Los quirófanos disponen de gran cantidad de aparatos médicos (respiradores, máquinas de oxígeno, etc.). Cada aparato médico está asignado a un único quirófano y se quiere saber cuántos hay de cada uno de ellos en cada quirófano. Dentro de cada planta los quirófanos nos vienen identificado por número de quirófano, el Q1, el Q2... y así sucesivamente.
- Los pacientes, de entrada, son atendidos en una visita realizada por un médico/a. Es posible que en visitas posteriores estos pacientes sean visitados por otro médico/a. Por cada visita habrá que guardar el diagnóstico, así como los medicamentos que le ha recetado, en su caso.
- Se quiere llevar un control de las visitas que los enfermos realizan a cada médico/a. Por eso y por cada día y por cada médico/a habrá que saber la hora de visita de cada uno de sus pacientes.
- También se quiere llevar un control de las reservas de habitaciones de los pacientes a ingresar. Por eso y por cada una de las habitaciones se quiere saber sus reservas, es decir día previsto de ingreso, día previsto de salida y de qué paciente se trata.
- Finalmente se quiere llevar un control de cada uno de los quirófanos y de las reservas previstas para realizar operaciones. Por eso y para cada uno de los quirófanos, se quiere saber por cada día y hora el médico que lo tiene reservado y el paciente al que se va a operar. No todos los pacientes que son ingresados deben operarse. Considere que cada operación la hace un solo médico y que es asistido por varios miembros del personal de enfermería.

# ROLES DE USUARIOS + SQL
