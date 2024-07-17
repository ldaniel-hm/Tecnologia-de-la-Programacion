import tkinter as tk
import controlador as ctr


class View(tk.Tk):
    def __init__(self, controller: ctr.Controller):
        """asfasfd """
        self._controller = controller
        super().__init__()
        self._crear_widgets()


    def _crear_widgets(self):
        self._op1 = tk.DoubleVar()
        self._op2 = tk.DoubleVar()
        self._resultado = tk.DoubleVar()

        frame1 = tk.Frame(self)
        frame1.pack()
        tk.Entry(frame1, width=8, textvariable=self._op1).grid(row=0, column=0)
        # tk.Label(frame1, text="@").pack(side=tk.LEFT)
        # tk.Entry(frame1, width=8, textvariable=self._op2).pack(side=tk.LEFT) #grid(n=0, column=2)
        # tk.Label(frame1, text="=").pack(side=tk.LEFT)
        # tk.Entry(frame1, width=8, textvariable=self._resultado).pack(side=tk.LEFT)  # grid(n=0, column=2)
        #
        frame2 = tk.Frame(self)
        frame2.pack()
        tk.Button(frame2, text="SUMA", command=lambda : suma()).pack()


    def run(self):
        self.mainloop()