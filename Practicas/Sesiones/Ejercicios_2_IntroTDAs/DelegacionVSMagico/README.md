```
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 29/9/2022
(C) Distribuye, si quieres, sin quitar la autoría
```


Se considera un TDA cuya representación es

```
struct rep {
    int peso
    secuencia contenedor
}
```

y con los operadores:

```
cardinal(d): int
    Indica el cardinal del contenedor del dato d

igual(d1, d2): bool
    Indica si d1 es igual que d2.
    Son iguales si tienen el mismo peso.

menor(d1, d2): bool
    Indica si d1 es menor que d2.
    d1 es menor que d2 si el peso de d1 es menor que el peso de d2
```


En el fichero TDA1.py se muestra una implementación incorrecta de este TDA en Python porque **no aprovecha** 
la potencia del lenguaje: no usa métodos mágicos. Podría ser una implementación correcta en otro lenguaje, 
pero no lo es en Python.

En el fichero TDA2.py se muestra una implementación correcta de este TDA en Python porque sí usa los métodos mágicos.

Recuerda: Python es un lenguaje orientado a objetos. TODO son objetos. Por tanto, cualquier operación que se haga 
(una suma, un producto, una comparación,...) conlleva a una invocación interna en el lenguaje a algún método. Es lo que le 
ocurre a la función `len()`, que invocará el método interno `__len__()`. Python nos da la opción de
definir nosotros mismos esos métodos, y a esos métodos que nos permiten usar ciertos operadores y funciones de una forma
mucho más cómoda de escribir son los métodos mágicos.
    - Es más cómodo escribir len(rep) que rep.cardinal()
    - Es más cómodo escribir d1==d2 que d1.igual(d2)
    - Es más cómodo escribir d1<d2 que d1.mentr(d2)
Si conoces los métodos mágicos de Python y los sobreescribes, tendrás unos TDAs que serán mucho más cómodos de manejar
en Python que en otros lenguajes.
