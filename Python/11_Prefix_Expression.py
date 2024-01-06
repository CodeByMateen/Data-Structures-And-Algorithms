class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:

  def __init__(self):
    self.front = None

  def enqueue(self, data):
    node = Node(data)
    if self.front is None:
      self.front = node
    else:
      current = self.front
      while current.next is not None:
        current = current.next
      current.next = node

  def dequeue(self):
    if self.front is None:
      return None
    else:
      current = self.front
      self.front = self.front.next
      return current.data

  def front(self):
    if self.front is None:
      return None
    else:
      return self.front.data

  def isEmpty(self):
    if self.front is None:
      return True
    else:
      return False

  def size(self):
    count = 0
    current = self.front
    while current is not None:
      count += 1
      current = current.next
    return count

  def printQueue(self):
    if self.front is None:
      print("Queue is empty")
    current = self.front
    while current is not None:
      print(current.data)
      current = current.next


if __name__ == '__main__':
  q = Queue()
  q.enqueue(5)
  q.enqueue(6)
  # print(q.size())
  # q.dequeue()
  q.printQueue()
