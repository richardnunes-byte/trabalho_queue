from queue import Queue


if __name__ == "__main__":
    fila = Queue(max_size=3)

    fila.enqueue("Item 1")
    fila.enqueue("Item 2")
    print(f"Fila após enqueues: {fila}")

    print(f"(peek): {fila.peek()}")

    print(f"Item removido: {fila.dequeue()}")
    print(f"Fila após dequeue: {fila}")

    print(f"is_empty {fila.is_empty()}")
    print(f"Tamanho da fila: {fila.size()}")

    fila.enqueue("Item 3")
    fila.enqueue("Item 4")


    fila.enqueue("Item 5") #tantando ultrapassar o limite da fila

    fila.clear()
    print(f"Fila após clear: {fila}")


    fila.dequeue() #tantando tirar itens de uma lista vazia
 