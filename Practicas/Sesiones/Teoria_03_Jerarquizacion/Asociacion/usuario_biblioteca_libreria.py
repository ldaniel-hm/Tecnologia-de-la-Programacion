"""
Un usuario está inscrito en una única biblioteca y en una única tienda de libros.
Tanto la biblioteca como la tienda contienen una cantidad ingente de libros, y tienen registrado al usuario como cliente.
Además todo libro agrega la biblioteca en la que se encuentra depositado y la tienda en la que fue comprado.
¿Qué debería de hacer el usuario para consultar la disponibilidad de un libro?
"""


class Libro:
    """"""
    def __init__(self, titulo: str):
        self._titulo = titulo
        self._biblioteca: Biblioteca = None  # Agregación de Biblioteca
        self._tienda: Tienda = None  # Agregación de Tienda
        self._estoy_disponible: bool = True

    def set_biblioteca(self, biblioteca_instance):
        self._biblioteca = biblioteca_instance

    biblioteca = property(fset=set_biblioteca)

    def set_tienda(self, tienda_instance):
        self._tienda = tienda_instance

    tienda = property(fset=set_tienda)

    def get_titulo(self):
        return self._titulo

    titulo = property(fget=get_titulo)

    def consultar_disponibilidad(self) -> bool:
        return self._estoy_disponible


class Biblioteca:
    def __init__(self):
        self._libros: set[Libro] = set() # Agregación de Libro
        self._usuarios: set[Usuario] = set() # Agregación de usuarios

    def append_libro(self, libro: Libro):
        self._libros.add(libro)  # Agregación de Libro
        libro.biblioteca = self # Establecer relación inversa con Libro

    def append_usuario(self, usuario: 'Usuario'):
        self._usuarios.add(usuario)  # Agregación de Usuario

    def consultar_disponibilidad(self, titulo: str):
        for e in self._libros:  # Type Libro
            if e.titulo == titulo:
                return e.consultar_disponibilidad()


class Tienda:
    def __init__(self):
        self._libros: set[Libro] = set() # Agregación de Libro
        self._usuarios: set[Usuario] = set() # Agregación de usuarios

    def append_libro(self, libro: Libro):
        self._libros.add(libro)  # Agregación de Libro
        libro.tienda = self # Establecer relación inversa con Libro

    def append_usuario(self, usuario: 'Usuario'):
        self._usuarios.add(usuario)  # Agregación de Usuario

    def consultar_disponibilidad(self, titulo: str):
        for e in self._libros:  # Type Libro
            if e.titulo == titulo:
                return e.consultar_disponibilidad()

"""
En un proyecto real, la clase Biblioteca y Tienda tendrían que redifinirse pues, 
como se puede comprobar, solo difieren en una línea.
"""


class Usuario:
    def __init__(self, biblioteca_instance, tienda_instance):
        self._biblioteca = biblioteca_instance  # Agregación de Biblioteca
        biblioteca_instance.append_usuario(self)  # Agregación de Usuario a la biblioteca
        self._tienda = tienda_instance  # Agregación de Tienda
        tienda_instance.append_usuario(self) # Agregación de Usuario a la tienda

    def buscar_libro(self, titulo: str):
        if self._biblioteca.consultar_disponibilidad(titulo):  # Delegación en Biblioteca
            return True
        return self._tienda.consultar_disponibilidad(titulo)  # Delegación en Tienda


# Programa principal
if __name__ == "__main__":
    biblioteca = Biblioteca()
    tienda = Tienda()
    libro = Libro("Luis")
    biblioteca.append_libro(libro)
    libro = Libro("Daniel")
    tienda.append_libro(libro)
    usuario = Usuario(biblioteca, tienda)

    # Realizar consulta de disponibilidad a través del Usuario
    print(usuario.buscar_libro("Luis"))  # Delega en Biblioteca y Tienda
    print(usuario.buscar_libro("Daniel"))  # Delega en Biblioteca y Tienda
    print(usuario.buscar_libro("Hernández"))  # Delega en Biblioteca y Tienda

