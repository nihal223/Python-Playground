import unittest
from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_reachable(self, s, d):
        q = []
        visited = [False]*self.V

        q.append(s)
        visited[s] = True

        while q:
            print(q)
            x = q.pop(0)

            if x == d:
                return True

            for y in self.graph[x]:
                if visited[y] == False:
                    visited[y] = True
                    q.append(y)

        return False


class Test(unittest.TestCase):
  def test_find_route(self):
      g = Graph(4)
      g.add_edge(0, 1)
      g.add_edge(0, 2)
      g.add_edge(1, 2)
      g.add_edge(2, 0)
      g.add_edge(2, 3)
      g.add_edge(3, 3)

      u = 1
      v = 3
      self.assertEqual(g.is_reachable(u, v), True)

      u = 3
      v = 1
      self.assertEqual(g.is_reachable(u, v), False)


if __name__ == "__main__":
  unittest.main()
