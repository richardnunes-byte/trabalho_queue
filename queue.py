from typing import Any, List, Optional


class Queue:


    def __init__(self, max_size: Optional[int] = None) -> None:
  
        self.__data: List[Any] = []
        self.__max_size: Optional[int] = max_size

    def enqueue(self, item: Any) -> None:

        if self.is_full():
            raise OverflowError(
                "Fila cheia! Não é possível adicionar mais elementos."
            )
        self.__data.append(item)

    def dequeue(self) -> Any:

        if self.is_empty():
            raise IndexError(
                "Fila vazia! Não há elementos para remover."
            )
        return self.__data.pop(0)

    def peek(self) -> Any:

        if self.is_empty():
            raise IndexError(
                "Fila vazia! Não há elementos para visualizar."
            )
        return self.__data[0]

    def is_empty(self) -> bool:

        return len(self.__data) == 0

    def is_full(self) -> bool:
   
        if self.__max_size is None:
            return False
        return len(self.__data) >= self.__max_size

    def size(self) -> int:

        return len(self.__data)

    def clear(self) -> None:

        self.__data.clear()

    def __repr__(self) -> str:
        return str(self.__data)