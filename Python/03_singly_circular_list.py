class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class SinglyCircular:

  def __init__(self):
    self.head = None

  def InsertAtHead(self, data):
    if self.head is None:
      self.head = Node(data)
      self.head.next = self.head
    else:
      temp = self.head
      newNode = Node(data)
      while temp.next != self.head:
        temp = temp.next
      temp.next = newNode
      newNode.next = self.head
      self.head = newNode

  def InsertAtTail(self, data):
    if self.head is None:
      self.head = Node(data)
      self.head.next = self.head
    else:
      temp = self.head
      newNode = Node(data)
      while temp.next != self.head:
        temp = temp.next
      temp.next = newNode
      newNode.next = self.head

  def DeleteAtHead(self):
    if self.head is None:
      print("List is empty")
    else:
      temp = self.head
      while temp.next != self.head:
        temp = temp.next
      temp.next = self.head.next
      self.head = self.head.next

  def DeleteAtTail(self):
    if self.head is None:
      print("List is empty")
    else:
      temp = self.head
      while temp.next.next != self.head:
        temp = temp.next
      temp.next = self.head

  def PrintList(self):
    if self.head is None:
      print("List is empty")
    else:
      temp = self.head
      while temp.next != self.head:
        print(temp.data, end=" -> ")
        temp = temp.next
      print(temp.data)

  def Search(self, data):
    if self.head is None:
      print("List is empty")
    else:
      temp = self.head
      while temp.next != self.head:
        if temp.data == data:
          return True
        temp = temp.next
      if temp.data == data:
        return True
      return False

  def Reverse(self):
    if self.head is None:
      print("List is empty")
    else:
      temp = self.head
      prev = None
      while temp.next != self.head:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
      temp.next = prev
      self.head = prev


if __name__ == "__main__":
  circular = SinglyCircular()
  circular.InsertAtHead(1)
  circular.InsertAtHead(2)
  circular.InsertAtHead(3)
  # circular.Reverse()
  circular.PrintList()
