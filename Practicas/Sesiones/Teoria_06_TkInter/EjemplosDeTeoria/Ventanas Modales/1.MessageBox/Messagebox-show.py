"""
Ventanas de diálogo para Mostrar mensajes.

Tipo de Mensaje -> Tipo de MessageBox
Información -> showinfo()
Error  -> showerror()
Warning -> showwarning()
"""


from tkinter import messagebox

messagebox.showinfo("Information", "Informative message")
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning", "Warning message")
