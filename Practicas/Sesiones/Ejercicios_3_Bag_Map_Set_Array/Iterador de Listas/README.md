```
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 13/9/2022
(C) Distribuye, si quieres, sin quitar la autoría
```

# Enunciado

Debes crear un contenedor `MiLista` que tenga como atributo único una lista. A parte de los métodos que te sean 
necesario para  desarrollar el resto del ejercicio, debes implementar el método `__iter__(self)` que retorne 
un objeto  de tipo `IteradorDeMiLista`.

La clase `IteradorDeMiLista` deberá tener los atributos `listRef`, `pos`. El primero se inicializa en el 
constructor y almacena una referencia a un objeto de tipo `MiLista`. El segundo también se inicializa en el 
constructor con valor cero (int). Además implementará los siguientes dos métodos:
* `__iter__(self)` que retorna una referencia a sí mismo.
* `__next__(self)` que retorna el elemento de `listRef` que se encuentra en la posición `pos`. 
Además se incrementa en +2 dicho valor. Si `pos` supera el número de elementos de la lista, ejecutará la 
sentencia `raise StopIteration`.

Con todo lo anterior ejecuta este código

```
miLista = MiLista([0,1,2,3,4,5,6,7,8])
for elem in miLista:
  print(elem)
```

El resultado debe ser:

```
0
2
4
6
8
```
