"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 30/10/2022

https://programmerclick.com/article/8047526022/


Un mixin es una clase que ofrece cierta funcionalidad para ser heredada por una subclase, pero que no está ideada para
ser autónoma. Si el lenguaje de programación lo permitiera debería escribirse como:
    class Hija extends Padre whit Mixin
para indicar que la clase Hija deriva de la clase Padre pero que hereda el Mixin.
El Mixin no debe entenderse como otra clase, sino como un conjunto de métodos que le son útiles a la clase Hija y
que ya están implementados. El código del Mixin no se sobreescribe.

En este ejemplo se tiene la clase Display con el método display() que muestra algo en pantalla.
Se quiere una clase hija MySubClass que hereda el método display() para seguir mostrando algo en la pantalla y con el
método nuevo log() que escribe algo en un fichero a la vez que se muestra en la pantalla.
Se considera entonces pertinente tener una clase/mixin con los métodos display() y log(), tal y como se indica en el
código, y que pueda ser usado no solo por MySubClass, sino por cualquier otra clase. La única condición es que la
clase que use el mixin debe tener implementado un método display() - que hará lo que considere oportuno. El mixin no
entra en su funcionamiento.
"""


class Displayer:
    """Displayer muestra un mensaje en consola"""
    def display(self, message):
        print(str(self), message)


class LoggerMixin:
    """Añade dos funcionalidades:
    - Escribe un mensaje en un fichero.
    - Muestra un mensaje en consola y lo escribe en un fichero de texto.
    """
    def log(self, message, filename='logfile.txt'):
        with open(filename, 'a') as fh:
            fh.write(message)

    def display(self, message):
        super().display(message)  # Donde se inyecte requiere el método display. No todos lo tienen.
        self.log(message)


class MySubClass(LoggerMixin, Displayer):
    """Hace log a un fichero delegando en la clase padre"""
    def log(self, message):
        super().log(message, filename='../subclasslog.txt')


subclass = MySubClass()
subclass.display("This string will be shown and logged in subclasslog.txt")