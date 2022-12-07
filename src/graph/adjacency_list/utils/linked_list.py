from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    """
    Estrutura de um nó. Ou vértice, seguindo a nomenclatura dos grafos.

        Parameters:
            data (str): Dado a ser armazenado no nó.
            next: Apontamento para o próximo nó da lista ligada.
    """

    data: Any
    next: Any = None

    def __repr__(self) -> str:
        return f'{self.data} -> {self.next}'


class LinkedList:
    """
    Implementa uma lista ligada do tipo FIFO.

        Parameters:
            head (Node): representa o primeiro elemento da lista ligada, a
            cabeça.
    """

    def __init__(self, head: Node = None):
        self.head = head

    def __is_empty(self):
        return True if not self.head else False

    def insert(self, node: Node):
        """
        Insere o nó passado como parâmetro na última posição da lista ligada, a
        calda.

            Returns:
                node (Node): nó que acabou de ser inserido.
        """
        if self.__is_empty():
            self.head = node
        else:
            next_node = self.head
            while next_node.next is not None:
                next_node = next_node.next
            next_node.next = node
        return node

    def remove(self):
        if self.__is_empty():
            return None
        else:
            next_node = self.head
            while next_node.next.next is not None:
                next_node = next_node.next
            del next_node.next

    def print(self):
        """
        Imprime o resultado final da lista ligada.
        """
        print(self.head)


if __name__ == '__main__':
    # Instânciando NÓS AVULSOS
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')

    # Instânciando a LISTA LIGADA
    linked = LinkedList()

    # INSERSÃO de elementos na lista
    linked.insert(a)
    linked.insert(b)
    linked.insert(c)
    linked.insert(d)
    linked.insert(e)

    # IMPRESSÃO a lista criada
    linked.print()

    # Demonstração de REMOÇÃO
    linked.remove()
    linked.print()
