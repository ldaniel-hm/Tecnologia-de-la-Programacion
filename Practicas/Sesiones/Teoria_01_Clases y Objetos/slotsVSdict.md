
```
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 8/12/2022
(C) Distribuye, si quieres, sin quitar la autoría
```

¿Qué es __dict__? ¿Qué es __slot__?
======


`object.__dict__` Es un diccionario u otro tipo de mapa usado para almacenar los atributos de un objeto (Si son
modificables). Así, como casos particulares tenemos:

* `modulo.__dict__` Es un diccionario que contiene la tabla de símbolos del módulo.
* `clase.__dict__` Es un diccionario que contiene la tabla de símbolos de la clase.
* `instancia.__dict__` Es un diccionario que contiene la tabla de símbolos de la instancia.

`dir([objecto])` Sin argumentos, retorna la lista de nombres en el ámbito local.
Con un argumento, intenta retornar una lista de atributos válidos para ese objeto.
La lista resultante está ordenada alfabéticamente.
Si el objeto tiene un método llamado `__dir__()`, éste será llamado y debe retornar la lista de atributos.
Si el objeto no provee de un método `__dir__()`, la función intenta obtener la información del atributo `__dict__` del
objeto, si está definido, y de su objeto tipo. La lista resultante no está necesariamente completa,
y puede ser inexacta cuando el objeto tiene una función `__getattr__()` personalizada.

`dir()` se comporta de forma distinta con diferentes tipos de objeto, ya que intenta producir la información más
relevante en vez de la más completa:

* Si el objeto es un módulo, la lista contiene los nombres de los atributos del módulo.
* Si el objeto es un tipo o una clase, la lista contiene los nombres de sus atributos, y recursivamente la de los
    atributos de sus clases base.
* En cualquier otro caso, la lista contiene los nombres de los atributos del objeto, los nombres de los atributos
    de su clase, y recursivamente los atributos de sus clases base.

 `dir()` se ofrece como una herramienta para uso en una terminal de forma interactiva y, por tanto, intenta ofrecer un
 grupo  interesante de nombres más que  uno rigurosamente definido, y su comportamiento detallado puede cambiar
 entre versiones. Por ejemplo, los atributos de metaclase no están en la lista resultante cuando el argumento es una clase.

`vars()`, `vars(object)`
Retorna el atributo `__dict__` para un módulo, clase, instancia o cualquier otro objeto con un atributo `__dict__`.
Los objetos como módulos o instancias tienen un atributo actualizable `__dict__`; <<< OJO
sin embargo, otros objetos pueden tener restricciones de escritura en sus atributos `__dict__`.
Sin un argumento, `vars()` funciona como `locals()`.

`getattr(object, name)`
Devuelve el valor del atributo name del objeto. El nombre debe ser una cadena. Si la cadena es el nombre de uno
de los atributos del objeto, el resultado es el valor de ese atributo.
Por ejemplo, getattr(x, 'foobar') es equivalente al valor de x.foobar.
Si el atributo nombrado no existe se genera AttributeError.

`locals()`
Actualiza y retorna un diccionario representando la tabla de símbolos locales actual.
Las variables libres son retornadas por locals() cuando ésta es llamada en bloques de funciones, pero no en bloques de clases.
A nivel de módulo, locals() y globals() son el mismo diccionario.
Nota: Si a una variable no se le asigna valor en una función, Python la considera libre y busca su valor en los niveles
superiores de esa función, empezando por el inmediatamente superior y continuando hasta el programa principal.
Si a la variable se le asigna valor en algún nivel intermedio la variable se considera no local y si se le asigna
en el programa principal la variable se considera global,

`globals()`
Devuelve el diccionario que implementa el espacio de nombres del módulo actual.
Para el código dentro de las funciones, esto se establece cuando se define la función y permanece igual
independientemente de dónde se llame a la función.

`object.__slots__` https://docs.python.org/3/reference/datamodel.html?highlight=__slot#slots
Permite declarar explícitamente miembros de datos (como propiedades) y denegar la creación de `__dict__` y `__weakref__`
(a menos que se declare explícitamente en `__slots__` o esté disponible en un padre).
Para declararlo explícitamente hay que poner `__slots__` = '__dict__', '__weakref__'.
Si se añade `__dict__` a `__slots__` se podrá asignar nuevas variables a los objetos.
Si no se añade `__weakref__` a `__slots__` no se permitrá el uso de refrencias débiles.
El espacio ahorrado con `__slots__` en vez de usar `__dict__` puede ser MUY SIGNIFICATIVO.
La velocidad de búsqueda de atributos también se puede mejorar significativamente.
La herencia múltiple con varios padres que usen `__slots__` se puede usar pero solo uno de los padres puede tener los
atributos creador pos slots (las otras clases base NO deben tener slots - raise TypeError.


Moraleja:
Si se quiere usar el diccionario de los atributos de las clases e instancias, se debe usar `clase.__dict__` o
`instancia.__dic__`, pero la forma correcta es mediante invocación `vars(instancia)` o `vars(clase)`.
En el caso del primero mostrará las variables de instancia, en el caso del segundo las variables de clase y de
instancia (incluidos métodos). En ambos casos mostrará aquellas que hayan sido utilizadas (pues `__dict__` se modifica en
tiempo de ejecución) y, por tanto, no sólo las que se creen nuevas para la instancia/clase sino todas las heredadas.
De la salida se pueden quitar los nombre/métodos especiales usando comprehensión (hay un ejemplo en las transparencias).
Si tuvieras alguna clase con `__slots__` conseguirás que Python vaya más rápido y evitarás el problema de crear atributos
que no existen; pero a cambio tendrás algún inconveniente: puedes tener algún problema si usas herencia múltiple con
slots. Además el diccionario `__dict__` habrá desaparecido. Si quieres usar `__dict__` lo mejor es quitar/comentar `__slots__`.

