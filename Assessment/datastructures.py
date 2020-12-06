import math
import algorithms as alg

class HashTable():
  def __init__(self):
    # creates table with 1000 entry slots
    self.table = [None] * 100

  def add(self, item):
    # if index does not contain a bucket, it creates one
    if (type(self.table[item.hash]) != Bucket):
      self.table[item.hash] = Bucket()
    # adds item to the bucket
    bucketIndex = len(self.table[item.hash].bucket)
    item.id = str(item.hash) + "-" + str(bucketIndex)
    self.table[item.hash].add(item)

  def delete(self, poiId):
    idParts = poiId.split("-")
    self.table[int(idParts[0])].delete(int(idParts[1]))

  def lookup(self, name=None, id=None):
    # calculates hash of word
    if (name != None):
      hash = POI.calcHash(name)
    # checks if the table contains a bucket at that location
      if (self.table[hash] != None):
        for item in self.table[hash].find(name=name):
          print(item)
      else:
        print("That POI does not exist.")
    elif (id != None):
      # splits the ID into the index of the bucket and its index within bucket
      idParts = id.split("-")
      if (type(self.table[int(idParts[0])]) == Bucket):
        print(self.table[int(idParts[0])].find(index=idParts[1]))
      else:
        print("That POI does not exist.")

  def __str__(self):
    # creates array to hold all items
    pois = []
    # puts all items into array
    for bucket in self.table:
      if (bucket != None):
        for item in bucket.bucket:
          pois.append(item)

    sortedPois = alg.insertion_sort(pois)
    poisStr = ""

    for poi in sortedPois:
      poisStr += f"{poi.id}\t{poi.name}\t{poi.type}\t{poi.description}\n"
    
    return poisStr

class Bucket():
  def __init__(self):
    self.bucket = []

  def add(self, item):
    self.bucket.append(item)

  def find(self, name=None, index=None):
    if (name != None):
      items = []
      for item in self.bucket:
        if (item.name == name):
          items.append(item)
      return items
    elif (index != None):
      return self.bucket[int(index)]

  def delete(self, index):
    # adjusts IDs of other POIs to match new indexes
    for i in range(index+1, len(self.bucket)):
      idParts = self.bucket[i].id.split("-")
      newId = idParts[0] + "-" + str(int(idParts[1])-1)
      self.bucket[i].id = newId
    # deletes POI
    del self.bucket[index]

class POI:
  def __init__(self, name, poiType, description):
    self.name = name
    self.type = poiType
    self.description = description
    self.id = None # ID is generated when it is added to its bucket
    self.hash = POI.calcHash(name)

  def calcHash(name):
    # each successive character will be of less value so that it will be roughly in alphabetical order to make the insertion sort quicker
    hash = 0
    letterMultiplier = 10000
    for char in name.lower():
      if (letterMultiplier != 1 and ord(char) >= 97 and ord(char) <= 122): # only looks at characters which are letters of the alphabet
        hash += ord(char) * letterMultiplier
        letterMultiplier /= 10
      else:
        break
    hash = math.floor((hash*(99/385420)) - (4801500/19271))
    return hash

  def __str__(self):
    string = f"{self.id}\t{self.name}\t{self.type}\t{self.description}"
    return string