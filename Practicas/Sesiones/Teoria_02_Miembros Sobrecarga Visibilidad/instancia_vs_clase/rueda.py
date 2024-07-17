"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 12/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

Ejemplo de los distintos tipo de métodos que puedes encontrar en un programa.

Sobre  cualquier clase se pueden definir estas variables:

{Métodos de instancia} (u objeto).
    - Son métodos cuyo primer parámetro es self.
    - En el bloque del método se usa self.
    - Hace referencia a las acciones que puede hacer un objeto.
    - Se accede a ellos mediante objeto.metodo()


{Métodos de clase}
    - Son métodos cuyo primer parámetro es cls.
    - En el bloque del método se usa cls.
    - Hace referencia a las acciones que puede hacer una clase.
    - Se debe de acceder a ellos mediante Clase.metodo()

{Métodos estáticos}
    - Son métodos que no tienen ni self ni cls.
    - Hace referencia a las acciones que se puede hacer independientemente de una clase y de un objeto.
    - Son como funciones, pero que las vinculamos a una clase.



Modela esta situación: Las ruedas se contemplan como cilindros, por lo que se caracterizan por un radio y una altura.
Se quiere saber cuántas ruedas se han creado durante la ejecución del programa. Además, se quieren tener métodos
factorías: uno que construya ruedas grandes y otro que construya ruedas chicas. Además de cada rueda se puede
conocer su volumen, pero como se contempla como un cilindro se quiere poner a disposición dicho método para usarse
en cualquier momento.
"""


class Rueda:
    """Clase Rueda. Se contempla como un cilindro."""

    cardinal: int = 0  # Variable de clase

    @staticmethod
    def volumen_cilindro(radio: float, altura: float) -> float:
        """
        Método estático para calcular volúmenes de cilindros.
        :param radio: El radio de la base del cilindro.
        :param altura:  La altura del cilindro.
        :return: Volumen del cilindro.
        """
        return 3.14 * radio ** 2 * altura

    @classmethod
    def incrementa(cls):
        """
        Método de clase que incrementa en una unidad el cardinal de las instancias creadas.
        """
        cls.cardinal += 1

    @classmethod
    def numero_ruedas(cls) -> int:
        """
        Método de clase que retorna el número de ruedas creadas.
        :return: El número de ruedas creadas.
        """
        return cls.cardinal # cls es la clase. Se puede usar cls.cardinal o Rueda.cardinal


    @classmethod
    def grande(cls) -> 'Rueda':
        """
        Método factoría.
        Construye ruedas grandes. Con valores por defecto.
        """
        return cls(40, 60)   # Invoca al constructor.

    # ¿Cómo sería para ruedas pequeñas?  ¡ Escríbelo !

    def __init__(self, radio: float, altura: float):
        """
        Inicializador de ruedas. Se contemplan como cilindros.
        :param radio: El radio de la base del cilindro.
        :param altura:  La altura del cilindro.
        """
        self._radio = radio
        self._altura = altura
        Rueda.incrementa()  # Invoca al método de clase.

    def volumen(self) -> float:
        """
        Método de instancia para calcular el volumen de una rueda. Debe de usar self.
        Aprovecha la existencia del método estático para calcular el volumen.
        Estaría mal volver a copiar aquí el cálculo del volumen. ¡¡No repitas código nunca!!
        :return: El volumen de esta rueda.
        """
        return Rueda.volumen_cilindro(self._radio, self._altura)

if __name__ == '__main__':
    rueda = Rueda(10, 10)
    print(f"El volumen de la rueda es {rueda.volumen()}")
    print(f"El volumen de la rueda es {Rueda.volumen_cilindro(10, 20)}")
    grande = Rueda.grande()
    print(f"El número de ruedas es {Rueda.numero_ruedas()}")







