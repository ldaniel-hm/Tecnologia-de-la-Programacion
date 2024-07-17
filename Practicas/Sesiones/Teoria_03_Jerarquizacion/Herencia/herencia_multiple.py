"""
SITUACIÓN
----------------------
Tenemos dos clase, cada uno con sus respectivos parámetros.
   - La clase A tiene un string.
   - La clase B tiene un entero.

Añadimos una tercera clase que herede de A y de B.
Quiero que el constructor en C inicialice con el string heredado de A y el entero heredado de B.
-----------------------


CONCEPTOS QUE NECESITO SABER
----------------------

- ¿Cuál es el orden en el que se heredarán los atributos? Ese orden se conoce con el método de clase .mro()
       Si se declara la clase C como C(A, B), y ejecutamos C.mro() el orden es el siguiente:
       [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

- ¿Cuál es la clase super de una clase?
       La clase super de una clase es la que aparece a continuación, según el orden mro()

       Si se declara la clase C como C(A, B) el super de cada clase, desde la perspectiva de C, es el siguiente:
           - Para la clase C su clase super es la clase A
           - Para la clase A su clase super es la clase B
           - Para la clase B la clase super es object

       Y esto es porque su MRO es
       [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

- ¿Cómo se puede invocar a una clase super de un clase?
       Se usa el método super() con o sin argumentos.

       Por defecto super() de una clase se irá a su inmediatamente superior según el MRO.
       Pero si se escribe super(Clase, self) si irá a la clase super de la clase indicada.

       Si se declara la clase C como C(A, B) se tiene el siguiente MRO
       [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

       Por tanto, si desde C se invoca a:
           - super() nos iremos a la clase A.
           - super(A, self) nos iremos a la clase B (porque B es la super de A según el MRO)
           - super(B, self) nos iremos a la clase object (porque object es la super de B según el MRO)
----------------------
"""




# %%

"""
Las clases A y B son clases padres de C.
C se construye usando los nombre explícitos de las clases.
Tiene el problema de que si se cambia el nombre de las clases hay que cambiar el código.
"""

class A:
    def __init__(self, string: str, *args):
        self.string = string


class B:
    def __init__(self, valor: int):
        self.valor = valor


class C(A, B):
    def __init__(self, string: str, valor: int):
        # El MRO es [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
        A.__init__(self, string)
        B.__init__(self, valor)

    def __str__(self):
        return f"{self.string}, {self.valor}"


print(C.mro())
print(C("hola", 50))






# %%

"""
Las clases A y B son clases padres de C.
C se construye
  - con super() inicializamos según A
  - con super(A, self) inicializamos según B
"""

class A:
    def __init__(self, string: str, *args):
        self.string = string


class B:
    def __init__(self, valor: int):
        self.valor = valor


class C(A, B):
    def __init__(self, string: str, valor: int):
        # El MRO es [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
        super().__init__(string, valor)  # Invoca al super de C según el MRO de C. Es la clase A.
        super(A, self).__init__(valor)  # Invoca al super de A según el MRO de C. Es la clase B.

    def __str__(self):
        return f"{self.string}, {self.valor}"


print(C.mro())
print(C("hola", 50))



#%%



"""
La clase Root es clase padre de A y de B.
Las clases A y B son clases padres de C.
Se tiene una estructura de diamante.
C se construye con super() al padre -A- según el mro, éste invoca al super() según el mro -B-, y este al super() 
según el mro -Root-.
"""


class Root:
    def __init__(self, real: float):
        self.real = real

class A(Root):
    def __init__(self, string: str, *args):
        # Si se invoca a la creación de A por sí sola, el super() será Root. Mira A.mro()
        # Si se invoca a la creación de A a partir del super de C, el super de A será B. Mira C.mro()
        super().__init__(*args) # Ojo, hay que mandarlo empaquetado. De otro modo se manda una tupla.
        self.string = string

class B(Root):
    def __init__(self, valor: int, *args):
        super().__init__(*args)  # Ojo, hay que mandarlo empaquetado. De otro modo se manda una tupla.
        self.valor = valor


class C(A, B):
    def __init__(self, real: float, string: str, valor: int):
        # MRO: [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Root'>, <class 'object'>]
        # Según el MRO, con super() deberé pasar primero el parámetro de A, después el de B y por último el de Root.
        super().__init__(string, valor, real)  # Invoca al super de C según el MRO de C. Es la clase A.

    def __str__(self):
        return f"{self.real}, {self.string}, {self.valor}"


print(C.mro())
print(C(2.1, "hola", 50))  # Introduzco los datos en el orden en que se invocará al super()


# ¿Pero

#%%


"""
La clase Root es clase padre de A y de B.
Las clases A y B son clases padres de C.
Se tiene una estructura de diamante.
¿y si quiero no pensar en el mro() y pensar solo en los parámetros? Pues hay que usar diccionarios
Cada clase recupera el atributo cuyo nombre coincida y manda a los demás como diccionario a la clase padre.
"""



class Root:
    def __init__(self, real: float = 0.0):
        self.real = real


class A(Root):
    def __init__(self, string: str = "", **kwargs):
        # Si se invoca a la creación de A por sí sola, el super() será Root. Mira A.mro()
        # Si se invoca a la creación de A a partir del super de C, el super de A será B. Mira C.mro()
        super().__init__(**kwargs) # Ojo, hay que mandarlo empaquetado. De otro modo se manda una tupla.
        self.string = string


class B(Root):
    def __init__(self, valor: int = 0, **kwargs):
        super().__init__(**kwargs)  # Ojo, hay que mandarlo empaquetado. De otro modo se manda una tupla.
        self.valor = valor


class C(A, B):
    def __init__(self, real: float = 0.0, string: str = "", valor: int= 0):
        # MRO: [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Root'>,
        # <class 'object'>] Según el MRO, con super() deberé pasar primero el parámetro de A, después el de B y por
        # último el de Root.
        super().__init__(real=real, string=string, valor=valor)  # Invoca al super de C según quiera yo

    def __str__(self):
        return f"{self.real}, {self.string}, {self.valor}"




print(C.mro())
print(C(valor=50, string="hola", real=2.1))  # Introduzco los datos en el orden que quiera

