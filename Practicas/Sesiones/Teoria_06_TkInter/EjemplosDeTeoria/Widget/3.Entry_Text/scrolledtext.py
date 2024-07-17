import tkinter as tk
from tkinter import scrolledtext
root = tk.Tk()

labelframe = tk.LabelFrame(root, text="Este es un LabelFrame")
labelframe.pack(fill="both", expand="yes")

txtbox = scrolledtext.ScrolledText(labelframe, width=40, height=10)
txtbox.pack(fill=tk.X, side=tk.LEFT, expand=True)

tk.mainloop()
