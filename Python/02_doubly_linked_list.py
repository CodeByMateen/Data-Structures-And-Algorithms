class Node:

  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None


class Doubly:

  def __init__(self):
    self.head = None

  def InsertAtHead(self, data):
    if self.head is None:
      self.head = Node(data)
    else:
      new_node = Node(data)
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def InsertAtTail(self, data):
    if self.head is None:
      self.head = Node(data)
    else:
      new_node = Node(data)
      temp = self.head
      while temp.next is not None:
        temp = temp.next
      temp.next = new_node
      new_node.prev = temp

  def InsertAtPosition(self, data, position):
    if self.head is None:
      self.head = Node(data)
    else:
      if position == 0:
        self.InsertAtHead(data)
      else:
        new_node = Node(data)
        temp = self.head
        count = 0
        while count < position - 1:
          temp = temp.next
          count += 1
        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp

  def DeleteAtHead(self):
    if self.head is None:
      print("List is empty")
    else:
      self.head = self.head.next
      self.head.prev = None

  def DeleteAtTail(self):
    if self.head is None:
      print("List is empty")
    else:
      temp = self.head
      while temp.next is not None:
        temp = temp.next
      temp.prev.next = None

  def DeleteAtPosition(self, position):
    if self.head is None:
      print("List is empty")
    else:
      if position == 0:
        self.DeleteAtHead()
      else:
        temp = self.head
        count = 0
        while count < position - 1:
          temp = temp.next
          count += 1
        temp.next = temp.next.next
        temp.next.prev = temp

  def Print(self):
    if self.head is None:
      print("List is empty")
    else:
      temp = self.head
      while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
        if temp:
          print(" <-> ", end="")
      print()

  def ReversePrint(self):
    if self.head is None:
      print("List is empty")
    else:
      temp = self.head
      while temp.next is not None:
        temp = temp.next
      while temp is not None:
        print(temp.data, end=" ")
        temp = temp.prev
      print()

  def Search(self, data):
    if self.head is None:
      print("List is empty")
    else:
      temp = self.head
      while temp is not None:
        if temp.data == data:
          print("Found")
          return
        temp = temp.next
      print("Not Found")


if __name__ == '__main__':
  doubly = Doubly()
  doubly.InsertAtHead(1)
  doubly.InsertAtHead(2)
  doubly.InsertAtTail(5)
  doubly.Print()
