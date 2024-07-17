from Ejercicios.ProductosRecursos.recursos import Carne, Coche, Pan
from Ejercicios.ProductosRecursos.interfaces import IProducto

if __name__ == '__main__':
    lista_productos = [Carne(20, "Soria"), Pan(.70,  60), Coche(12000, 1)]
    print(IProducto.precio_final(lista_productos))
