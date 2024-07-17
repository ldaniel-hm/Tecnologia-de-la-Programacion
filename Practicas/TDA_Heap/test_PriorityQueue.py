from TDA_Heap.PriorityQueue import   PriorityQueue

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cola = PriorityQueue()
    print(f"Añadiendo, en este orden: 50 20 10")
    cola.add(50)
    cola.add(20)
    cola.add(10)
    print("Cola Actual:", cola)
    print(f"Sacando a: {cola.pop()}")
    print("Cola Actual:", cola)

