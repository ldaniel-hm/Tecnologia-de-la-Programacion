"""
Ventanas de diálogo para preguntar y seleccionar entre varias opciones:

Opciones a mostrar -> Tipo de MessageBox
No, Yes -> askquestion(), askyesno()
Cancel , Ok -> askokcancel()
Cancel , Retry -> askretrycancel()
Cancel, No, Yes -> askyesnocancel()
"""


from tkinter import messagebox

answer = messagebox.askquestion("Question", "Are you learning?")
# No = False, Yes = True
print(answer)

answer = messagebox.askyesno("Question", "Do you like Python?")
# No = False, Yes = True
print(answer)

answer = messagebox.askokcancel("Question", "Do you want to open this file?")
# Cancel = False, Ok = True
print(answer)

answer = messagebox.askretrycancel("Question", "Do you want to try that again?")
# Cancel = False, Retry = True
print(answer)

answer = messagebox.askyesnocancel("Question", "Continue playing?")
# Cancel = None, No = False, Yes = True
print(answer)