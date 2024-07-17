s = "global"

def f():
    s = "local"
    print("Estoy en f(). A la variable se le asigna un valor nuevo: ", s, id(s))

def g():
    global s
    s = "globalmente modificada"
    print("Estoy en g(). A la variable se le asigna un valor nuevo: ",s, id(s))


if __name__ == '__main__':
    print("\n\nMuestra la variable con su valor inicial.", s, id(s))
    f()
    print("Después de f(). El identificador local es distinto al global. Y no cambia el valor del global: ", s, id(s))
    g()
    print("Después de g(). El identificador local es el mismo que el de global. Sí cambia el valor del global: ", s, id(s))
