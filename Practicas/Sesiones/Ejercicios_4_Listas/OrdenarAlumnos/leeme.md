```
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 16/10/2022
(C) Distribuye, si quieres, sin quitar la autoría
```


# Enunciado

Crea la clase **Acta**. 
El acta de una asignatura es un documento que consta de una lista donde, en cada fila, figura un alumno junto con la 
calificación obtenida. Para este ejercicio se supondrá que todos los alumnos tienen una calificación numérica real en el 
intervalo [0,10] y con un valor decimal. Se pide:

- Crea un conjunto de no menos de 10 alumnos. 
No es importante que los datos de los alumnos tengan sentido, lo importante es que se distingan. 
Puedes usar un bucle _for_ para acelerar el proceso.

- Construye entonces un acta con esos alumnos y asigna a cada uno una nota aleatoria.
Recurre al módulo https://docs.python.org/es/3/library/random.html

- Ordena a los alumnos del acta de acuerdo a sus calificaciones.
Mira los métodos mágicos de comparación **\_\_cmp\_\_()**, **\_\_lt\_\_()**, **\_\_qt\_\_()*, etc.
A efectos de depuración, necesitarás que todos los alumnos tengan siempre la misma calificación ``aleatoria''  
en cada ejecución. Para conseguir que en cada ejecución siempre se generan los mismos números aleatorios 
usa siempre la misma semilla, p.e. \cm{seed(0)}.

- Construye un diccionario que indique cuántos alumnos han suspendido (nota < 5), han aprobado (5<= nota < 7), 
tienen notable (7<= nota < 9) o son de sobresaliente (nota >= 9).
