class Graph:
    def __init__(self, v):
        # Adjancy matrix for weigted graph storing
        self.graph = [[0] * (v+1) for _ in range(v+1)]
        # Creating start vertex to rows and end vertex to column
        for i in range(v+1):
            self.graph[i][0] = i
            self.graph[0][i] = i

    def addEdge(self, u, v, w):
        # Adding edge to graph with vertices u, v connected with weight w
        self.graph[u][v] = w

    def find_smallest_path(self, a, b):
        
        return []

    def printGraph(self):
        for i in self.graph:
            for j in i:
                print(j, end=" ")
            print()

if __name__ == '__main__':
    t = int(input())    # Number Test Cases

    for _ in range(t):
        result = []
        # Reading Number of Vertices, Edges and Questions
        vertices, edges, questions = map(int, input().split())
        graph_obj = Graph(vertices)

        for _ in range(edges):
            # Reading input for edge with vertices u, v connected with weight w
            u, v, w = map(int, input().split())
            graph_obj.addEdge(u,v,w)
        print("")
        graph_obj.printGraph()
        print("")
        for _ in range(questions):
            # Finding 𝑘-th maximum weight in path of a -> b
            a, b, k = map(int, input().split())
            print(a, b)
            path = graph_obj.find_smallest_path(a, b)

    