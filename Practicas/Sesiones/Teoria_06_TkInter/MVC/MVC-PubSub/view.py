import tkinter as tk


class View(tk.Tk):

    def __init__(self, controller):
        super().__init__()
        self._controller = controller
        self.title("Calculadora")
        self._make_widgets()

    def main(self):
        self.mainloop()

    def _make_widgets(self):
        self._op1_var = tk.DoubleVar()
        self._op2_var = tk.DoubleVar()
        self._total_var = tk.DoubleVar()

        main_frm = tk.Frame(self)
        main_frm.pack(padx=10, pady=10)
        tk.Entry(main_frm, width=8, textvariable=self._op1_var).grid(row=0, column=0)
        tk.Label(main_frm, text=" + ").grid(row=0, column=1)
        tk.Entry(main_frm, width=8, textvariable=self._op2_var).grid(row=0, column=2)
        tk.Label(main_frm, text=" = ").grid(row=0, column=3)
        tk.Entry(main_frm, state="readonly", width=8, textvariable=self._total_var).grid(row=0, column=4)

        second_frm = tk.Frame(self)
        second_frm.pack(padx=10, pady=10)

        captions = ["SUMAR", "MULTIPLICAR"]
        for caption in captions:
            self._ent = tk.Button(second_frm, text=caption,
                                  command=lambda btn=caption:
                                  self._controller.operar(btn, self._op1_var.get(), self._op2_var.get()))
            self._ent.pack(side='left')

    @property
    def resultado(self):
        pass

    @resultado.setter
    def resultado(self, valor: float):
        self._total_var.set(valor)


