```
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 6/9/2022
(C) Distribuye, si quieres, sin quitar la autoría
```

# Enunciado


Implementa el TDA fecha usando la representación indicada en un ejemplo de los apuntes. 
Para ello debes completar el siguiente código:

```
class Fecha:
    __slots__ = '_dia', '_mes', '_agno'

    def __init__(self, dia: int, mes: int, agno: int):
        pass

    def _set_agno(self, agno: int) -> None:
        pass

    def _set_mes(self, mes: int) -> None:
        pass

    def _set_dia(self, dia: int, mes: int) -> None:
        pass

    def get_dia(self) -> int:
        pass

    def get_mes(self) -> int:
        pass

    def get_agno(self) -> int:
        pass

    def __str__(self) -> str:
        pass
```


Ten en cuenta que:

* `def __init__()` debe invocar a los métodos `def _set_xxx`. Por ejemplo, se invocará a la asignación del año como `self._set_agno(agno)`.

* Los métodos `def _set_xxx` controlarán si los argumentos son correctos, en especial para los días (que dependen de los meses).
Usa las instrucciones `assert` y `isinstance` para generar un error si los valores dados no se corresponden con la especificación. 
No es necesario comprobar que los años sean bisiestos.
Observa que empiezan con ``guión bajo''. Esto quiere decir que los métodos `_set_xxx} no deberían ser invocados desde otras clases (es decir, no se puede modificar una fecha una vez creada). 

* Crea fechas válidas y crear fechas inválidas.


La solución se encuentra en los ficheros .py.

