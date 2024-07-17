"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 14/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Ejemplo de uso
"""


from TDA_Date.DateSimple import Date
from TDA_Map.MapList import Map
from Alumno import Alumno
from Alumnos import Alumnos
from Asignatura import Asignatura
from Asignaturas import Asignaturas


def main():
    luis: Alumno = Alumno('Luis', 'Hernández', '120812', Date(1, 1, 2001))
    daniel: Alumno = Alumno('Daniel', 'Rubio', '93472', Date(2, 2, 2002))
    elena: Alumno = Alumno('Elena', 'García', '9347462', Date(3, 3, 2003))
    maria: Alumno = Alumno('Maria', 'Sánchez', '938473', Date(4, 4, 2004))

    # Mostramos a los alumnos que acabamos de construir
    print(luis, daniel, elena, maria, sep='\t')


    logica: Asignatura = Asignatura(1001, 'Lógica', 1)
    analisis: Asignatura = Asignatura(1002, 'Análisis', 1)
    programacion: Asignatura = Asignatura(1003, 'Programación', 1)
    automatas: Asignatura = Asignatura(2001, 'Autómatas', 2)
    poo: Asignatura = Asignatura(2002, 'POO', 2)
    ia: Asignatura = Asignatura(3001, 'Inteligencia Artificial', 3)
    # No hay asignatuas de cuarto curso

    # Mostramos las asignaturas que acabamos de construir
    print(logica, analisis, programacion, automatas, poo, ia, sep='\t')

    # Creaos un conjunto de asignaturas con las asignaturas individuales.
    asignaturas: Asignaturas = Asignaturas()
    asignaturas.add(logica)
    asignaturas.add(analisis)
    asignaturas.add(programacion)
    asignaturas.add(automatas)
    asignaturas.add(poo)
    asignaturas.add(ia)

    # Mostramos el conjunto de asignatuas
    print ("Conjunto de asignturas", asignaturas, sep='\n')

    cursos: Map = asignaturas.asignaturas_por_curso()
    print("Asignaturas por cursos", cursos, sep='\n')

    # Matriculamos a los alumnos en las asignaturas
    luis.add_asignatura(logica)  # Primero
    luis.add_asignatura(analisis)
    luis.add_asignatura(programacion)
    daniel.add_asignatura(automatas)  # Segundo
    daniel.add_asignatura(poo)
    elena.add_asignatura(logica)  # Primero y segundo
    elena.add_asignatura(analisis)
    elena.add_asignatura(automatas)
    maria.add_asignatura(ia)  # Tercero

    # Y añadimos cada alumno al conjunto de alumnos
    alumnos: Alumnos = Alumnos()
    alumnos.add(luis)
    alumnos.add(daniel)
    alumnos.add(elena)
    alumnos.add(maria)

    print("Alumnos por cursos", alumnos.alumnado_por_curso(), sep='\n')

    print("Alumnos por asignaturas", alumnos.alumnado_por_asignaturas(asignaturas), sep='\n')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
