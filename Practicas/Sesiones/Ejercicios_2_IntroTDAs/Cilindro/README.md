```
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 6/9/2022
(C) Distribuye, si quieres, sin quitar la autoría
```


# Enunciado y soluciones


## Enunciado

Se quiere construir el TDA Cilindro Recto con las operaciones básicas del cálculo de volumen y superficie.

* Defina el TDA

### Solución
```
TDA Cilindro
------------

* Representa a los cilindros rectangulares, dados por su radio y altura.
* Usa: reales (R)
* Operaciones:
   * Crear (real radio, real altura): Cilindro
     Precondiciones: radio y altura deben ser positivos.
     Retorna: Construye un cilindro con el radio y altura dados.
              Un cilidro queda caracterizado por su radio y altura.
   * Area(Cilindro c) : real
     Dado un cilindro c retorna el área/superficie de c.
   * Volumen(Cilindro c) : real
     Dado un clindro c retorna el volumen de c.
```

## Enunciado

Defina la función de abstracción

### Solución

Se definirá la función de abstracción Abst: **rep** -> *A*, 
siendo **rep** una estructura que consta de dos campos:
```
struct rep {
   float radio
   float altura
}
```

Abst(rep) se identifica con el cilindro con radio rep.radio y altura rep.altura. 


## Enunciado 

Defina el invariante de la representación.

### Solución
El invariante de la representación es un predicado I:**rep** --> *B* que debe ser cierto cuando la 
representación represente a un objeto correcto y falso en otro caso. Podemos definirla de este modo:
```
I(r) = r.radio > 0 AND r.altura > 0
```


## Enunciado

* Implemente en Python el TDA.
* Añada a la implementación el método mágico \pyv{__str__()} para imprimir toda la información disponible de un cilindro.

### Solución

Está en el código adjunto.

