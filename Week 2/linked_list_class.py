class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

  def link(self, otherNode):
    self.next = otherNode 
    otherNode.prev = self

  def __str__(self):
    return self.data

class LinkedList:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def add(self, node):
    if (self.last == None):
      self.first = node
      self.last = node
    else:
      node.prev = self.last
      self.last.next = node
      self.last = node
    self.length += 1

  def get(self, index):
    if (index > (self.length-1)):
      return("Error: index out of range")
    elif (index > (self.length/2)):
      temp = self.last
      for i in range(self.length-index-1):
        temp = temp.prev
      return(temp.data)
    else:
      temp = self.first
      for i in range(index):
        temp = temp.next
      return(temp.data)


x = LinkedList()
n1 = Node("node 1")
n2 = Node("node 2")
n3 = Node("node 3")
n4 = Node("node 4")
n5 = Node("node 5")
x.add(n1)
x.add(n2)
x.add(n3)
x.add(n4)
x.add(n5)