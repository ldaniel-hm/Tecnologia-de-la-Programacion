import tkinter as tk

root = tk.Tk()
root.geometry("300x100+200+200")
root.title("Label")


button1 = tk.Button(root, text="Pos. absoluta")
button1.place(x=10, y=10, width=290, height=50)

button2 = tk.Button(root, text="Pos. realativa")
button2.place(relx=.5, rely=.5, relwidth=.5, relheight=.5)

tk.mainloop()
