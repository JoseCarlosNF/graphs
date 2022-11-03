class Vertex:
    """
    Define um vértice.

    label (Any): Define como um vértice será identificado.
    """

    def __init__(self, label: any) -> None:
        self.label = label

    def __repr__(self) -> str:
        return f'{self.label}'


class Edge:
    """
    Define uma aresta.

    vertices (tuple[Vertex, Vertex]): Tupla com os dois vértices que foram a
    aresta.

    weight (int): Define o peso de uma aresta para os grafos ponderados. Se
    um valor não for passado, é dado como nulo (None).
    """

    def __init__(
        self, vertices: tuple[Vertex, Vertex], weight: int = None
    ) -> None:
        self.vertices = vertices
        self.weight = weight

    def __repr__(self) -> str:
        return (
            f'{__class__.__name__}: '
            f'{self.vertices}, '
            f'weight: {self.weight}'
        )
