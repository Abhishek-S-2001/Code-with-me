class Graph:
    def __init__(self, v):
        # Adjancy matrix for weigted graph storing
        self.graph = [[0] * v for _ in range(v)]

    def printGraph(self):
        for i in self.graph:
            for j in i:
                print(j, end=" ")
            print()

if __name__ == '__main__':
    t = int(input())

    n, m, questions = map(int, input().split())
    graph_obj = Graph(4)
    graph_obj.printGraph()

    
