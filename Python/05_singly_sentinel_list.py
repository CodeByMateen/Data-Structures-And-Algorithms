class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class SinglySentinel:

  def __init__(self):
    self.head = Node(None)
    self.tail = Node(None)
    self.head.next = self.tail

  def AddNodeAtStart(self, data):
    temp = Node(data)
    if self.head.next == self.tail:
      self.head.next = temp
      temp.next = self.tail
    else:
      temp.next = self.head.next
      self.head.next = temp

  def AddNodeAtEnd(self, data):
    temp = Node(data)
    if self.head.next == self.tail:
      self.head.next = temp
      temp.next = self.tail
    else:
      ptr = self.head
      while ptr.next != self.tail:
        ptr = ptr.next
      temp.next = self.tail
      ptr.next = temp

  def DeleNodeAtStart(self):
    if self.head.next == self.tail:
      print("List is empty")
    else:
      self.head.next = self.head.next.next

  def DeleNodeAtEnd(self):
    if self.head.next == self.tail:
      print("List is empty")
    else:
      ptr = self.head
      while ptr.next.next != self.tail:
        ptr = ptr.next
      ptr.next = self.tail

  def PrintList(self):
    ptr = self.head
    while ptr != self.tail:
      print(ptr.data, end=" -> ")
      ptr = ptr.next
    print(self.tail.data)

  def ReverseList(self):
    if self.head.next == self.tail:
      print("List is empty")
    else:
      prev = self.head
      curr = self.head.next
      while curr != self.tail:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
      self.head.next = prev
      self.tail.next = None


if __name__ == "__main__":
  sentinel = SinglySentinel()
  sentinel.AddNodeAtStart(3)
  sentinel.AddNodeAtStart(1)
  sentinel.AddNodeAtEnd(4)
  sentinel.AddNodeAtEnd(7)
  sentinel.AddNodeAtEnd(9)
  sentinel.AddNodeAtEnd(0)
  sentinel.PrintList()
  sentinel.ReverseList()
  sentinel.PrintList()
