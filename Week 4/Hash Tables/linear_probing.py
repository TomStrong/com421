class HashTable():
  def __init__(self):
    # creates table with 127 entry slots
    self.table = [None] * 127

  def add(self, item):
    # if index contains an item, goes through the list until a free slot is found
    tempIndex = item.hash
    while (self.table[tempIndex] != None):
      tempIndex += 1
    # adds item to list
    self.table[tempIndex] = item

  def lookup(self, name):
    # calculates hash of word
    name = name.lower()
    hash = Item.calcHash(name)
    # checks if the table contains a bucket at that location
    if (self.table[hash] != None):
      while (self.table[hash].name != name):
        hash += 1
      print(self.table[hash])
    else:
      print("That is not stored in the dictionary.")

class Item():
  def __init__(self, name, val):
    # creates item instance
    self.name = name.lower()
    self.value = val
    self.hash = Item.calcHash(name)

  def calcHash(name):
    # creates a hash by adding the ascii values of each character
    hash = 0
    for char in name:
      hash += ord(char)
    hash = hash % 127
    return hash

  def __str__(self):
    string = self.name + ": " + self.value
    return string


table = HashTable()
item1 = Item("cat", "4 legged animal that goes 'Meow'")
item2 = Item("dog", "4 legged animal that goes 'Woof'")
item3 = Item("act", "test")
table.add(item1)
table.add(item2)
table.add(item3)
table.lookup("act")
table.lookup("dog")
table.lookup("cat")
table.lookup("test")
print(table.table)
table.lookup("test")
print(table.table[58])
print(table.table[59])
print(table.table[60])