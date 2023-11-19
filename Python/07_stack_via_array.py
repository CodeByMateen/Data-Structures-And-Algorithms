class Stack:

  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if len(self.items) == 0:
      return "Stack is Empty"
    return self.items.pop()

  def peek(self):
    if len(self.items) == 0:
      return "Stack is Empty"
    return self.items[len(self.items) - 1]

  def size(self):
    return len(self.items)

  def printStack(self):
    print(self.items)


if __name__ == "__main__":
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.pop()
  stack.pop()
  stack.printStack()
  print(stack.peek())