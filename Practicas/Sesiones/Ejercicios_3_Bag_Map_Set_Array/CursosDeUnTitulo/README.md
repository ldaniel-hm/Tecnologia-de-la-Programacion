```
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 6/9/2022
(C) Distribuye, si quieres, sin quitar la autoría
```

# Enunciado


Para este ejercicio usa tu implementación del TDA Map y del TDA Set limitándote al uso de los operadores del TDA. 
Si alguno no lo has implementado usa entonces la estructura de datos **dict** y **set** que te ofrece {Python}.

Implementa las siguientes clases con las especificaciones que se indican:

* Asignatura. Una asignatura se caracterizará por un nombre, código numérico de la asignatura y curso en el que se 
imparte (un número entre 1 y 4). Estos 3 atributos se pueden consultar. 
Dos asignaturas son iguales si tienen el mismo código (implementa el método *\_\_eq\_\_()*).

* Asignaturas. Representa a un conjunto de asignaturas. Se pueden añadir asignaturas al conjunto y puede calcular un 
* diccionario cuya clave es el curso y el valor es el conjunto de asignaturas de dicho curso.

* Alumno. Cada alumno se caracteriza por tener un nombre y apellido, un número de identificación y 
una fecha de nacimiento (es un TDA). Cada alumno se matricula de un conjunto de asignaturas
(de tipo **Asignaturas**) que pueden ser de distintos cursos. La lista de asignaturas de un alumno se puede consultar.

* Alumnos. Es un conjunto de alumnos al que se le pueden añadir alumnos.
Puede retornar un diccionario con clave igual al curso y valor el conjunto de alumnos que están matriculados en ese curso. 
También puede calcular un diccionario con clave igual al código de una asignatura y cuyo valor es el conjunto 
de alumnos matriculados en dicha asignatura. Observa que para este segundo diccionario tendrás que suministrar 
por parámetro la lista de asignaturas.

Construye una función auxiliar que calcule el conjunto de alumnos que están matriculados en una asignatura 
(dada por su código) y úsala para el segundo diccionario.


Para comprobar el funcionamiento correcto de tus clases construye 6 asignaturas y las almacenas en una variable de 
tipo  **Asignaturas**. Comprueba que se pueden calcular las asignaturas de cada curso.

Construye también 4 alumnos y asígnales algunas asignaturas de las 6 construidas anteriormente. 
Almacénalos en una variable de tipo **Alumnos** y construye los dos diccionarios que pueden calcularse en esta clase.
