def sin_grid():
    import tkinter as tk

    root = tk.Tk()
    root.title("Probando Entry")
    frame = tk.Frame(root, width=350, height=200)
    frame.pack()

    tk.Label(frame, text="Escribe algo:").pack(side=tk.LEFT)
    tk.Entry(frame).pack(side=tk.RIGHT)

    root.mainloop()


if __name__ == "__main__":
    sin_grid()
