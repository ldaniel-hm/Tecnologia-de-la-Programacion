import vista
from modelo import Model


class Controller:
    def __init__(self):
        self._model = Model()
        self._view = vista.View(self)

    def run(self):
        self._view.run()


if __name__ == '__main__':
    controller = Controller()
    controller.run()
