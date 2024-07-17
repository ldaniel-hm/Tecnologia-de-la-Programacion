fichero = "telefonos.txt"
min_len_tlf = 9


def menu() -> str:
    string="1. Añadir teléfono\n2. Borrar teléfono\n0. Terminar"
    ok = False
    opcion = '0'
    while not ok:
        print(string)
        opcion: str = input("Dame una opción: ")
        if 0 <= int(opcion) <= 2:
            ok = True
        else:
            print('Prueba de nuevo.')
    return opcion


def tlf_ok(telefono: str, min_len: int) -> bool:
    if len(telefono) < min_len:
        while len(telefono) < min_len:
            telefono = '0' + telefono
    return telefono


def telefonos_sin_nl(fichero: str) -> list:
    try:
        with open(fichero, "r") as f:
            telefonos=f.readlines()
        telefonos = [tlf[:-1] for tlf in telefonos]
    except IOError:
        telefonos = []

    return telefonos


def exists(fichero: str, telefono: str) -> bool:
    telefonos = telefonos_sin_nl(fichero)
    return telefono in telefonos


def add(fichero: str, telefono: str):
    if exists(fichero, telefono):
        return

    with open(fichero, "a") as f:
        print(telefono, file=f)


def remove(fichero: str, telefono: str):
    telefonos=telefonos_sin_nl(fichero)

    try:
        telefonos.remove(telefono)  # Lanza una exception si no está
    except ValueError:
        return
    else:
        with open(fichero, "w") as f:
            telefonos = [tlf + '\n' for tlf in telefonos]
            f.writelines(telefonos)


def main():
    otra_vez = True
    while otra_vez:
        opc = menu()
        if opc == '0':
            otra_vez = False
        else:
            tlf = input("Dame un nuevo número: ")
            if opc == '1':
                add(fichero, tlf_ok(tlf, min_len_tlf))
            else:
                remove(fichero, tlf_ok(tlf, min_len_tlf))


if __name__ == "__main__":
    main()
