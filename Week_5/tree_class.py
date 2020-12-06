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