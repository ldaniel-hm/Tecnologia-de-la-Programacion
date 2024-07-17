from model import Model
from view import View


class Controller:
    def __init__(self): # , view: View, model: Model):
        self._model = Model()
        self._view = View(self)

    def main(self):
        self._view.main()

    def operar(self, string: str, op1: float, op2: float):
        if string == 'SUMAR':
            self._view.resultado = self._model.suma(op1, op2)
        if string == 'MULTIPLICAR':
            self._view.resultado = self._model.multiplica(op1, op2)


if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
