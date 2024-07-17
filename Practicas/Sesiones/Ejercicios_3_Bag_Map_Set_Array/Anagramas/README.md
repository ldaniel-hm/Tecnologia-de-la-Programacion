```
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 16/3/2024
(C) Distribuye, si quieres, sin quitar la autoría
```

# Enunciado

Dada una lista de palabras, se te pide que agrupes las palabras que sean anagramas entre sí. Dos palabras son anagramas si contienen las mismas letras, pero en un orden diferente. Por ejemplo, "amor" y "roma" son anagramas. Para ello se considera la siguiente solución:

- Como estructura de datos se usará la clase `AnagramFinder` que consta de un campo que es un diccionario. También tienen los métodos `.add_word()` que añade una palabra al diccionario y `.return_anagrams()` que retorna los anagramas.

- Como solución, se considera el siguiente programa principal.

  1. Considerara una lista de palabras. Por ejemplo:

  2. Construye un objeto de la clase `AnagramFinder`.

  3. Para cada palabra construir una clave/valor y añadirla al diccionario del objeto construido en el paso anterior:
      - Ordenar las letras de la palabra alfabéticamente.
      - Usar la palabra ordenada como una clave y agregar la palabra original al valor correspondiente a esa clave. El valor es un bag.

4. Imprime los anagramas invocando al método del objeto que retorna los anagramas.



Como ejemplo considera las siguientes palabras de entrada.
```python
words = ["ramo", "amor", "roma", "perro", "pera", "arco", "carro", "mar", "ram", "casa", "saca",
         "tarde", "dater", "paso", "sopa", "roca", "caro", "rima", "mira"]
```

