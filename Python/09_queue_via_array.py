class Queue:

  def __init__(self):
    self.items = []

  def enqueue(self, data):
    self.items.append(data)

  def dequeue(self):
    if not self.isEmpty():
      return self.items.pop(0)
    else:
      print("Queue is empty")

  def size(self):
    return len(self.items)

  def front(self):
    return self.items[0]

  def isEmpty(self):
    return self.size() == 0

  def printitems(self):
    print(self.items)


if __name__ == '__main__':
  q = Queue()
  q.enqueue(4)
  q.enqueue(4)
  q.enqueue(5)
  print(q.front())
  q.printitems()
