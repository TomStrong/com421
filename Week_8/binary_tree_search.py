class BinaryTree():
  def __init__(self):
    self.root = None

  def insert(self, node):
    if (self.root == None):
      self.root = node
    else:
      self.traverseTree(self.root, node)
      
  def traverseTree(self, lastNode, node):
    if (lastNode.value > node.value):
      if (lastNode.left != None):
        nextNode = lastNode.left
        self.traverseTree(nextNode, node)
      else:
        lastNode.left = node
    elif (lastNode.value < node.value):
      if (lastNode.right != None):
        nextNode = lastNode.right
        self.traverseTree(nextNode, node)
      else:
        lastNode.right = node


class TreeNode():
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value 


class Queue:
  def __init__(self, capacity):
    self.array = [None] * capacity
    self.start = 0
    self.end = capacity - 1
    self.size = 0

  def add(self, value):
    # get next index
    if (self.end != (len(self.array) - 1)):
      temp = self.end + 1
    else:
      temp = 0
    # add new item if queue is not full
    if (self.array[temp] == None):
      self.end = temp
      self.array[self.end] = value
      self.size += 1
      #print("{} has been added to the queue.".format(value.value))
    else:
      print("Queue is full!")
  
  def remove(self):
    #print(self.array[self.start].value)
    self.array[self.start] = None
    self.size -= 1
    # update start index
    if (self.start != (len(self.array) - 1)):
      self.start += 1
    else:
      self.start = 0


def run():
  newTree = BinaryTree()
  newTree.insert(TreeNode(5))
  newTree.insert(TreeNode(1))
  newTree.insert(TreeNode(8))
  newTree.insert(TreeNode(6))
  newTree.insert(TreeNode(9))
  newTree.insert(TreeNode(3))
  newTree.insert(TreeNode(10))
  newTree.insert(TreeNode(4))
  newTree.insert(TreeNode(2))
  newTree.insert(TreeNode(7))

  value = int(input("Enter search value: "))
  valueFound = False
  searchingList = Queue(10)
  searchingList.add(newTree.root)

  while (valueFound == False):
    if (searchingList.array[searchingList.start].value == value):
      print("Found")
      break
    else:
      if (searchingList.array[searchingList.start].left != None):
        searchingList.add(searchingList.array[searchingList.start].left)
      if (searchingList.array[searchingList.start].right != None):
        searchingList.add(searchingList.array[searchingList.start].right)

      searchingList.remove()
      if (searchingList.array[searchingList.start] == None):
        print("Not found")
        break
    

run()