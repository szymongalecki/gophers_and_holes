class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def coordinates(self):
        return (self.x, self.y)


class Gopher(Point):
    def __repr__(self):
        return f"Gopher @ ({self.x}, {self.y})"


class Hole(Point):
    def __repr__(self):
        return f"Hole @ ({self.x}, {self.y})"


class Graph:
    def __init__(self, g: int, h: int, s: int, v: int):
        self.g = g
        self.h = h
        self.max_range = s * v
        self.gophers = []
        self.holes = []
        self.graph = []
        self.matching = []
        self.add_gophers()
        self.add_holes()
        self.create_graph()

    def result(self):
        return self.g - self.maximum_bipartite_matching()

    def create_graph(self):
        self.graph = [[None] * len(self.holes) for _ in range(len(self.gophers))]
        for g, gopher in enumerate(self.gophers):
            xg, yg = gopher.coordinates()
            for h, hole in enumerate(self.holes):
                xh, yh = hole.coordinates()
                distance = ((xg - xh) ** 2 + (yg - yh) ** 2) ** (0.5)
                if distance <= self.max_range:
                    self.graph[g][h] = hole

    def bipartite_matching(self, g, match, visited):
        for h, _ in enumerate(self.holes):
            if self.graph[g][h] != None and visited[h] == False:
                visited[h] = True
                if match[h] == None or self.bipartite_matching(
                    match[h], match, visited
                ):
                    match[h] = g
                    self.matching = match
                    return True
        return False

    def maximum_bipartite_matching(self):
        match = [None] * len(self.holes)
        result = 0
        for g, _ in enumerate(self.gophers):
            visited = [False] * len(self.holes)
            if self.bipartite_matching(g, match, visited):
                result += 1
        return result

    def reconstruct_matching(self):
        for h, g in enumerate(self.matching):
            if g != None:
                print(f"{self.gophers[g]} -> {self.holes[h]}")

    def add_gophers(self):
        for _ in range(self.g):
            x, y = [float(_) for _ in input().split()]
            self.gophers.append(Gopher(x, y))

    def add_holes(self):
        for _ in range(self.h):
            x, y = [float(_) for _ in input().split()]
            self.holes.append(Hole(x, y))

    def __repr__(self) -> str:
        repr = "\n"
        col_width = max(len(str(word)) for row in self.graph for word in row) + 2
        for row in self.graph:
            repr += "".join(str(word).ljust(col_width) for word in row) + "\n"
        return repr


g, h, s, v = [int(_) for _ in input().split()]
graph = Graph(g, h, s, v)
print(graph)
print(
    f"Max # of Gophers that can be matched to Holes - {graph.maximum_bipartite_matching()}\n"
)
graph.reconstruct_matching()
