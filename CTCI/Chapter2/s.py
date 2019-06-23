class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))


print(count)