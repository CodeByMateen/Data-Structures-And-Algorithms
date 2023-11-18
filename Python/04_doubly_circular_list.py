class Node:

  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None


class DoublyCircular:

  def __init__(self):
    self.head = None

  def InsertAtHead(self, data):
    if self.head is None:
      self.head = Node(data)
      self.head.next = self.head
      self.head.prev = self.head
    else:
      temp = Node(data)
      temp.next = self.head
      temp.prev = self.head.prev
      self.head.prev.next = temp
      self.head.prev = temp
      self.head = temp

  def InsertAtTail(self, data):
    if self.head is None:
      self.head = Node(data)
      self.head.next = self.head
      self.head.prev = self.head
    else:
      temp = Node(data)
      temp.next = self.head
      temp.prev = self.head.prev
      self.head.prev.next = temp
      self.head.prev = temp

  def DeleteAtHead(self):
    if self.head is None:
      print("List is empty")
    else:
      if self.head.next == self.head:
        self.head = None
      else:
        self.head.prev.next = self.head.next
        self.head.next.prev = self.head.prev
        self.head = self.head.next

  def DeleteAtTail(self):
    if self.head is None:
      print("List is empty")
    else:
      if self.head.next == self.head:
        self.head = None
      else:
        temp = self.head.prev
        temp.prev.next = self.head
        self.head.prev = temp.prev

  def PrintList(self):
    if self.head is None:
      print("List is empty")
    else:
      temp = self.head
      while temp.next != self.head:
        print(temp.data, end=" <-> ")
        temp = temp.next
      print(temp.data)

  def ReversePrintList(self):
    if self.head is None:
      print("List is empty")
    else:
      temp = self.head.prev
      while temp.prev != self.head.prev:
        print(temp.data, end=" <-> ")
        temp = temp.prev
      print(temp.data)


if __name__ == "__main__":
  circular = DoublyCircular()
  circular.InsertAtHead(1)
  circular.InsertAtHead(2)
  circular.InsertAtHead(3)
  circular.InsertAtTail(4)
  circular.InsertAtTail(5)
  circular.InsertAtTail(6)
  circular.PrintList()
  circular.ReversePrintList()
