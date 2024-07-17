import tkinter as tk


def label_text_pack():
    """
    Varias etiquetas de texto usando pack()
    """
    # Ventana
    root = tk.Tk()
    root.geometry("350x200+100+100")
    root.title("Probando Label")

    # Frame
    frame = tk.Frame(root, width=350, height=200)
    frame.pack()

    # Etiqueta
    tk.Label(frame, text="¡Hola Mundo!").pack(anchor='nw')
    tk.Label(frame, text="¡Otra etiqueta muy muy larga!").pack(anchor='center')
    tk.Label(frame, text="¡Última etiqueta!").pack(anchor='se')

    root.mainloop()


def label_text_place():
    """
    Una etiqueta formada por una línea de texto usando place().
    """

    # Ventana
    root = tk.Tk()
    root.title("Probando Label")
    root.geometry("350x200+100+100")

    # Frame
    frame = tk.Frame(root, width=350, height=200)
    frame.pack()

    # Etiqueta en el frame
    label = tk.Label(frame, text="Esto es una prueba")
    label.place(x=50, y=100)
    label.config(fg="yellow", bg="blue")
    label.config(font=("Verdana", 24))

    root.mainloop()


def label_imagen():
    """
    Una etiqueta formada por una imagen usando place().
    """

    # Ventana
    root = tk.Tk()
    root.title("Probando Label con Imagen")
    root.geometry("350x200+100+100")

    # Frame
    frame = tk.Frame(root, width=350, height=200)
    frame.pack()

    # Etiqueta en el Frame
    mi_imagen = tk.PhotoImage(file="ldaniel.png")
    label = tk.Label(frame, image=mi_imagen)
    label.place(x=50, y=40)

    root.mainloop()


if __name__ == "__main__":
    label_text_pack()
    label_text_place()
    label_imagen()
