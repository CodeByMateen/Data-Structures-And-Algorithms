class Node:

  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None


class DoublySentinel:

  def __init__(self):
    self.head = Node(None)
    self.tail = Node(None)
    self.head.next = self.tail
    self.tail.prev = self.head

  def InsertAtEnd(self, data):
    node = Node(data)
    node.next = self.head.next
    node.prev = self.head
    self.head.next.prev = node
    self.head.next = node

  def InsertAtEnd(self, data):
    node = Node(data)
    node.next = self.tail
    node.prev = self.tail.prev
    self.tail.prev.next = node
    self.tail.prev = node

  def DeleteAtEnd(self):
    if self.head.next == self.tail:
      return
    self.head.next = self.head.next.next
    self.head.next.prev = self.head

  def DeleteAtEnd(self):
    if self.head.next == self.tail:
      return
    self.tail.prev = self.tail.prev.prev
    self.tail.prev.next = self.tail

  def PrintList(self):
    ptr = self.head
    while ptr != self.tail:
      print(ptr.data, end=" <-> ")
      ptr = ptr.next
    print(self.tail.data)

  def PrintListReverse(self):
    ptr = self.tail
    while ptr != self.head:
      print(ptr.data, end=" <-> ")
      ptr = ptr.prev
    print(self.head.data)


if __name__ == "__main__":
  sentinel = DoublySentinel()
  sentinel.InsertAtEnd(4)
  sentinel.InsertAtEnd(5)
  sentinel.InsertAtEnd(6)
  sentinel.InsertAtEnd(3)
  sentinel.InsertAtEnd(2)
  sentinel.InsertAtEnd(1)
  sentinel.PrintList()
  sentinel.DeleteAtEnd()
  sentinel.PrintList()
  sentinel.PrintListReverse()
