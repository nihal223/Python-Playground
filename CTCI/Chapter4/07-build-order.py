import unittest
from collections import defaultdict
import operator


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_egde(self, v1, v2):
        self.graph[v1].append(v2)

    def build_graph(self, projects, dependencies):
        for pair in dependencies:
            self.add_egde(pair[0], pair[1])
        for node in projects:
            if node not in self.graph:
                self.add_egde(node, None)
        return self

    def find_first_node(self):
        count = defaultdict(int)
        for i in self.graph.items():
            count[i[0]] = len(i[1])

        return max(count.items(), key=operator.itemgetter(1))[0]


def build_order(graph):
    q = []
    visited = [False]*128
    res = []

    s = graph.find_first_node()

    q.append(s)
    visited[ord(s)] = True

    while q:
        x = q.pop(0)
        res.append(x)
        for y in graph.graph[x]:
            if y is not None:
                if visited[ord(y)] != True:
                    q.append(y)
                    visited[ord(y)] = True

    for i in graph.graph.items():
        if i[0] not in res:
            res.append(i[0])

    return res


class Test(unittest.TestCase):
    def test_build_order(self):
        projects = ['a', 'b', 'c', 'd', 'e', 'f']
        dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
        graph = Graph(len(projects))
        graph = graph.build_graph(projects, dependencies)

        self.assertEqual(build_order(graph), ['f', 'b', 'a', 'd', 'c', 'e'])


if __name__=='__main__':
    unittest.main()