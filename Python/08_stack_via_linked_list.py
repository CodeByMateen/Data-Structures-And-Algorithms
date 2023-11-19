class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:

  def __init__(self):
    self.top = None

  def push(self, data):
    if self.top is None:
      self.top = Node(data)
    else:
      temp = self.top
      while temp.next is not None:
        temp = temp.next
      temp.next = Node(data)

  def pop(self):
    if self.top is None:
      return "Stack is Empty"
    elif self.top.next is None:
      self.top = None
    else:
      temp = self.top
      while temp.next.next is not None:
        temp = temp.next
      temp.next = None

  def peek(self):
    temp = self.top
    while temp.next is not None:
      temp = temp.next
    print(temp.data)

  def printStack(self):
    if self.top is None:
      print("Stack is empty")
      return
    node = self.top
    while node is not None:
      print(node.data, end=" ")
      node = node.next
    print()

  def size(self):
    if self.top is None:
      return 0
    node = self.top
    count = 0
    while node is not None:
      count += 1
      node = node.next
    print(count)

  def reverseStack(self):
    if self.top is None:
      return
    prev = None
    node = self.top
    while node is not None:
      next = node.next
      node.next = prev
      prev = node
      node = next
    self.top = prev


if __name__ == "__main__":
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  stack.printStack()
  stack.peek()
  stack.reverseStack()
  stack.printStack()
  stack.size()
  stack.peek()
