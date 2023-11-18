class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class Singly:

  def __init__(self):
    self.head = None

  def InsertAtHead(self, data):
    if self.head is None:
      self.head = Node(data)
    else:
      temp = Node(data)
      temp.next = self.head
      self.head = temp

  def InsertAtTail(self, data):
    if self.head is None:
      self.head = Node(data)
    else:
      temp = self.head
      while temp.next is not None:
        temp = temp.next
      temp.next = Node(data)

  def DeleteAtHead(self):
    if self.head is None:
      print("List is empty")
    else:
      self.head = self.head.next

  def DeleteAtTail(self):
    if self.head is None:
      print("List is empty")
    else:
      temp = self.head
      while temp.next.next is not None:
        temp = temp.next
      temp.next = None

  def Print(self):
    if self.head is None:
      print("List is empty")
    else:
      temp = self.head
      while temp:
        print(temp.data, end="")
        temp = temp.next
        if temp:
          print(" -> ", end="")
      print()

  def Reverse(self):
    if self.head is None:
      print("List is empty")
    else:
      prev = None
      curr = self.head
      while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
      self.head = prev

  def ReverseRecursive(self, prev, curr):
    if curr is None:
      self.head = prev
      return
    next = curr.next
    curr.next = prev
    self.ReverseRecursive(curr, next)


if __name__ == "__main__":
  singly = Singly()
  singly = Singly()
  singly.InsertAtHead(5)
  singly.InsertAtHead(4)
  singly.InsertAtHead(3)
  singly.InsertAtHead(2)
  singly.InsertAtHead(1)
  singly.InsertAtTail(0)
  singly.Print()
  singly.ReverseRecursive(None, singly.head)
  singly.Print()
