from dataclasses import dataclass, field
from typing import Any

from utils.linked_list import LinkedList, Node


@dataclass
class Vertex:
    data: Any
    adjacency_list: LinkedList = field(default_factory=LinkedList)

    def __repr__(self) -> str:
        return f'{self.data}'


@dataclass
class Edge:
    origin: Vertex
    destination: Vertex
    weight: int = 0

    def __repr__(self) -> str:
        return f'({self.weight}) -> {self.destination}'


class Graph(LinkedList):
    """
    Implementação de grafo baseada em listas ligadas.
    """

    def __init__(self, root: Vertex = None, directed: bool = False):
        self.vertices = []
        self.root = root
        self.directed = directed

    def add_edge(self, origin: Vertex, destination: Vertex, weight: int = 0):
        """
        Adiciona uma relação entre dois vértices do grafo.

        Caso o grafo não seja dirigido, a relação é replicada nos dois
        elementos. Do contrário, apenas o elemento de origem terá a relação
        aplicada.
        """
        if not self.directed:
            destination.adjacency_list.insert(
                Node(data=Edge(destination, origin, weight))
            )
        origin.adjacency_list.insert(
            Node(data=Edge(origin, destination, weight))
        )

    def add_vertex(self, vertex: Vertex):
        """
        Insere um novo vertice ao grafo, mas não associa a nenhum vertice.
        """
        self.vertices.append(vertex)

    def print(self):
        for vertex in self.vertices:
            print(f'[{vertex.data}] {vertex.adjacency_list.__dict__}')



if __name__ == '__main__':
    # Cria vertices soltos. Sem relacionamentos
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')

    # Define qual vertice será utilizado para contruir o grafo
    graph = Graph()
    graph.add_vertex(a)
    graph.add_vertex(b)
    graph.add_vertex(c)

    # Cria o primeiro realacionamento entre os vértices
    graph.add_edge(a, b, 1)
    graph.add_edge(a, c, 2)
    graph.add_edge(c, b, 3)

    breakpoint()

    graph.print()
