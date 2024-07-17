#from QueueList import Queue
from QueueArray import Queue
#from QueueLinked import Queue



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cola = Queue()
    print(f"Añadiendo, en este orden: 0, 1, 2")
    cola.push(0)
    cola.push(1)
    cola.push(2)
    print("Cola Actual:", cola)
    print(f"El primero que saldrá será: {cola.peek()}")
    print(f"Sacando a: {cola.pop()}")
    print("Cola Actual:", cola)
    print(f"Sacando a: {cola.pop()}")
    print("Cola Actual:", cola)
