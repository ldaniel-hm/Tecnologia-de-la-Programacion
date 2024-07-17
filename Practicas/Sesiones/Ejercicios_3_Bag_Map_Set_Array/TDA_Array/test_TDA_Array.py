#from TDAArrayPythonList import Array1D, Array2D, Matrix  # Arrays con listas de Python. Genera tú este fichero.

from TDAArrayPyObject import Array1D, Array2D, Matrix # Arrays con py_objects de Pytnhon



def test_array1d():
    print("Test Array1D\n"+"-"*20)
    mi_array = Array1D(3)  # Creación de un array de 3 elementos
    print("Test len()", mi_array, f"Tiene longitud {len(mi_array)}")  # check init, str, len

    print("Test set item. Asignando valores")
    for i in range(len(mi_array)):  # Check set item
        mi_array[i] = i * 10

    print("Test get()", [ mi_array[i] for i in range(len(mi_array)) ] )  # Check get item

    print("Test iterador")
    for value in mi_array:  # Check iterator
        print(value)

    print("Test contains")
    print("Está el 10 en el array:", 10 in mi_array)  # Check iterator
    print("Está el 5 en el array:", 5 in mi_array)  # Check iterator


def test_array2d():
    print("\nTest Array2D\n"+"-"*20)
    mi_array: Array2D = Array2D(2, 4, 2)  # Building an array2D (4-rows and columns 2, 4 ,6, 2)
    print(f"Test len(). Valores almacenados: {len(mi_array)}")

    print("Test set item. Asignando valores")
    # Asignación de  'datos  aleatorios'
    for i in range(mi_array.num_rows()):
        for j in range(mi_array.num_cols(i)):
            mi_array[i, j] = (i+1) * 10 + (j+1)  # Check set_item

    print("Test get()", [ mi_array[i, j] for i in range(mi_array.num_rows()) for j in range(mi_array.num_cols(i)) ] )  # Check get_item

    print("Test iterador")
    for value in mi_array:  # Check iterator
        print(value)

    print("Test contains")
    print("Está el 22 en el array:", 22 in mi_array)  # Check iterator
    print("Está el 5 en el array:", 5 in mi_array)  # Check iterator


def test_matrix():
    print("\nTest Matrix\n" + "-" * 20)
    matrix: Matrix = Matrix(3, 4)
    print(matrix)


if __name__ == "__main__":
    test_array1d()
    test_array2d()
    test_matrix()

