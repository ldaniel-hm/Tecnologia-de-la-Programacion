"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 12/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

En un clase "tradicional" todo atributo tendrá, para cada atributo:
    - uno o varios métodos para recuperar su valor. Estos métodos se llaman métodos Getter del atributo.
    - uno o varios métodos para cambiar su valor. Estos métodos se llaman métodos Setter del atributo.

Por ejemplo, para el atributo `luz: bool` de una casa se puede tener 1 método GET que se puede llamar `luz_encendida()`
para saber si la luz está encendida y puede tener 3 métodos SET para cambiar su estado: `encender()`, `apagar()`,
`cambiar_estado_luces(nuevo_valor)`.

Lo más usual es que exista uno o ningún método Setter, y uno o ningún método Getter.

En los ejemplos que vienen a continuación supondremos que existe un solo método SET y un solo método GET
"""


class MiClaseTradicional:
    """
    En esta clase se definen los métodos Get/Set de la forma tradicional, la forma estándar de hacerlo en cualquier
    lenguaje de programación.
        - Para recuperar el valor del atributo habrá que escribir `objeto.get_atributo()`
        - Para cambiar el valor del atributo habrá que escribir `objeto.set_atributo(valor)`
    Lo tradicional es que el nombre de los métodos se llamen igual que el del atributo.
    Si el atributo se llamara `x` entonces los métodos deberían llamarse `get_x()` y `set_x(valor)`.
    Siempre puedes cambiar el nombre del método, pero lo más normal es indicarlo como se indica.

    Nota: Los métodos Get/Set nunca deben usar print(). Aquí solo se usa por motivos docentes.
    """

    def __init__(self, un_x: str):
        self._x: str = un_x

    def get_x(self) -> str:
        print(f"Invocado el método GET de la clase {self.__class__}")
        return self._x

    def set_x(self, nuevo_x: str):
        print(f"Invocado el método SET de la clase {self.__class__}")
        self._x = nuevo_x


class MiClaseFuncionProperty:
    """
    En esta clase se definen los métodos Get/Set de la forma tradicional, la forma estándar de hacerlo en cualquier
    lenguaje de programación.
        - Para recuperar el valor del atributo habrá que escribir `objeto.get_atributo()`
        - Para cambiar el valor del atributo habrá que escribir `objeto.set_atributo(valor)`

    Ahora añadimos la instrucción `propiedad = property(fget=..,fset=..)`. Con esto estamos añadiendo una propiedad.
    Una propiedad es un miembro de la clase (como lo son los atributos, métodos, clases internas, ...)
    Una propiedad es un mecanismo con el que se puede leer, escribir o calcular el valor de un campo privado.
    Por tanto, una propiedad, si se define, sirve para gestionar el acceso a un atributo privado (y todos los
    atributos deben ser privados).
    Una propiedad es un miembro público que se usa como si fuera un campo (atributo o variable) pero realmente es un
    método especial que sirve para gestionar un atributo.

    Definida la propiedad, su uso es el siguiente:

        * Para recuperar el valor del atributo habrá que escribir `objeto.propiedad`.
            - `objeto.propiedad` invocará al método que se definió en el parámetro fget=.. de property()
            - Si se definió `propiedad = property(fget=funcionA, ...)`, entonces:
                    `objeto.propiedad` es equivalente a `objeto.funcionA()`

        * Para cambiar el valor del atributo habrá que escribir `objeto.propiedad = valor`.
            - `objeto.propiedad=valor` invocará al método que se definió en el parámetro fset=.. de property()
            - Si se definió `propiedad = property(fset=funcionB, ...)`, entonces:
                    `objeto.propiedad=valor` es equivalente a `objeto.funcionB(valor)`

        * Además, como el objetivo de una propiedad es servir de acceso a un campo privado, las funciones `funcionA`
        y `funcionB` deben de ser algún método GET y SET de dicho campo.

    En la práctica, si un campo se llama `_atributo` (para indicar que está oculto) su correspondiente propiedad,
    si se define, se suele llamar `atributo` (para indicar que hace referencia a una campo que se llama igual que él,
    pero que tiene un guion bajo).

    Si el atributo se llamara `_x` lo normal es que los métodos get/set se llamen get_x() y set_x(valor).
    Si el atributo se llamara `_x` lo normal es que su propiedad se llame x=property(...)
    Si juntamos las dos cosas, lo normal es escribir x = property(fset=set_x, fget=set_y)

    Nota: Los métodos Get/Set nunca deben usar print(). Aquí solo se usa por motivos docentes.
    """

    def __init__(self, un_x: str):
        self._x: str = un_x

    def get_x(self) -> str:
        print(f"Invocado el método GET de la clase {self.__class__}")
        return self._x

    def set_x(self, nuevo_x: str):
        print(f"Invocado el método SET de la clase {self.__class__}")
        self._x = nuevo_x

    x = property(fset=set_x, fget=get_x)




class MiClassDecoracionProperty:
    """
    En esta clase se muestra una forma alternativa al uso de `propiedad = property(fset=.., fget=..)`.
    Ahora lo que hacemos es usar una decoración que se llama @property.
    Cuando se antepone esta decoración a un método estamos indicando que dicho método pasa a ser una propiedad.
    Y si es una propiedad su función es servir de acceso a un campo (privado).
    En concreto, @property indica que el acceso es del tipo GET.
    Así, su uso debe ser el siguiente si se tiene en cuenta que el nombre de la propiedad debe ser igual que el del
    campo al que accede (pero sin el primer guión bajo):

        @property
        def atributo(self):
            return self._atributo

    Para decorar el método que actuará de propiedad SET se usa la decoración @atributo.setter y su uso es:

        @atributo.setter
        def atributo(self, valor):
            self._atributo = valor

    Esta es la única forma en la que habrás visto en Python la posibilidad de hacer sobrecarga. Aparace el mismo
    método `atributo()` definido dos veces con una cantidad diferente de parámetros de entrada. Con (self) y con
    (self, valor)
    """

    def __init__(self, un_x: str):
        self._x: str = un_x

    @property
    def x(self) -> str:
        print(f"Invocando a la propiedad -get- de {self.__class__}")
        return self._x

    @x.setter
    def x(self, nuevo_x: str):
        print(f"Invocando a la propiedad -set- de {self.__class__}")
        self._x = nuevo_x




class Descriptor:
    def __get__(self, instance, owner):
        return instance._attribute     # Obteniendo el valor del atributo
    def __set__(self, instance, value):
        instance._attribute = value    # Asignando un valor al atributo
    def __delete__(self, instance):
        del instance._attribute	    # Eliminando el atributo


class MiClassDescriptor:
    """
    En esta clase se muestra una forma alternativa al uso de propiedades.
    Consiste en usar un descriptor.
    En Python, un descriptor es un objeto que implementa uno o más de los métodos especiales __set__(), __get__(), __delete__().
    Cuando se accede al atributo del objeto o de la clase, si éste es un descriptor, Python invoca al método
    correspondiente __set__(), __get__(), __delete__() del descriptor.
    """

    x = Descriptor()  # Atributo de clase.

    def __init__(self, x: str):
        self.x = x  # Método set via descriptor. Attr de objeto
        self.__class__.x = 100  # Método set via descriptor. Attr de clase



def uso_tradicional():
    cosa: MiClaseTradicional = MiClaseTradicional("Tradicional")
    print(f"Valor inicial = {cosa.get_x()}")
    cosa.set_x("Tradicional modificado")
    print(f"Nuevo valor = {cosa.get_x()}")


def uso_property():
    cosa: MiClaseFuncionProperty = MiClaseFuncionProperty("Property")
    print(f"Valor inicial = {cosa.x}")
    cosa.x = "Property modificado"
    print(f"Nuevo valor = {cosa.x}")


def uso_decoracion():
    cosa: MiClassDecoracionProperty = MiClassDecoracionProperty("Decoración")
    print(f"Valor inicial = {cosa.x}")
    cosa.x = "Decoración modificado"
    print(f"Nuevo valor = {cosa.x}")


def uso_descriptor():
    cosa: MiClassDescriptor = MiClassDescriptor("Descriptor")
    print(f"Valor inicial = {cosa.x}")
    cosa.x = "Descriptor modificado"
    print(f"Nuevo valor = {cosa.x}")

    cosa2: MiClassDescriptor = MiClassDescriptor("Descriptor")
    print(f"Valor inicial = {cosa2.x}")
    cosa2.x = "Descriptor modificado por segunda vez"
    print(f"Nuevo valor = {cosa2.x}")
    print(f"Nuevo valor = {cosa.x}")

    print(MiClassDescriptor.x)



if __name__ == '__main__':
    metodos = [uso_tradicional, uso_property, uso_decoracion, uso_descriptor]
    for m in metodos:
        print('=' * 30)
        m()
        print('=' * 30)
