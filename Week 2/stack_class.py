class Stack:
    def __init__(self):
      self.array = []

    def push(self,value):
      self.array.append(value)

    def pop(self):
      if len(self.array) == 0:
        temp = "a is empty"
      else:
        temp = self.array[-1]
        del self.array[-1]
      return temp

    def __str__(self):
      return self.array.__str__()

stack1 = Stack()
stack1.push(1)
stack1.push(4)
stack1.push(9)
print(stack1)

print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())