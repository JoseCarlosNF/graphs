from graph import Vertex, Edge

if __name__ == '__main__':
    a = Vertex(2)
    b = Vertex('a')

    ab = Edge((a, b), 0)

    print(ab)
