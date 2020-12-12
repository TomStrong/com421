import math
import algorithms as alg

class HashTable():
  def __init__(self):
    # creates table with 100 entry slots
    self.table = [None] * 100
    self.count = 0

  def add(self, item):
    # if index does not contain a bucket, it creates one
    if (type(self.table[item.hash]) != Bucket):
      self.table[item.hash] = Bucket()
    # adds item to the bucket
    bucketIndex = len(self.table[item.hash].bucket)
    item.id = str(item.hash) + "-" + str(bucketIndex)
    self.table[item.hash].add(item)
    self.count += 1

  def delete(self, pID):
    idParts = POI.validateID(pID)
    if (idParts):
      if (type(self.table[idParts[0]]) == Bucket):
        self.table[idParts[0]].delete(idParts[1])
        self.count -= 1
        # removes bucket if it is empty
        if (len(self.table[idParts[0]].bucket) == 0):
          self.table[idParts[0]] = None
      else:
        print("Invalid ID")
    else:
      print("Invalid ID format.")

  def lookup(self, name=None, pID=None):
    if (name != None):
      if (POI.validateName(name)):
        hash = POI.calcHash(name)
        # checks if the table contains a bucket at that location
        if (self.table[hash] != None):
          itemList = []
          for item in self.table[hash].find(name=name):
            itemList.append(item)
          
          return itemList
        else:
          return "That POI does not exist."
      else:
        return "A name must have letters in it."
    elif (pID != None):
      idParts = POI.validateID(pID)
      if (idParts):
        if (type(self.table[int(idParts[0])]) == Bucket):
          return self.table[int(idParts[0])].find(index=idParts[1])
        else:
          return "That POI does not exist."
      else:
        return "Invalid POI ID format."

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
    # checks if index exists
    if (len(self.bucket) >= index + 1):
      # adjusts IDs of other POIs to match new indexes
      for i in range(index+1, len(self.bucket)):
        idParts = POI.validateID(self.bucket[i].id)
        newId = str(idParts[0]) + "-" + str(idParts[1]-1)
        self.bucket[i].id = newId
      # deletes POI
      del self.bucket[index]
      print("POI deleted.")
    else:
      print("Invalid ID")

class POI:
  def __init__(self, name, poiType, description):
    self.name = name
    self.type = poiType
    self.description = description
    self.id = None # ID is generated when it is added to its bucket
    self.hash = POI.calcHash(name)

  def validateName(name):
    if (name.lower().islower()):
      return True
    else:
      return False

  def validateID(pID):
    try:
      idParts = pID.split("-")
      idParts[0] = int(idParts[0])
      idParts[1] = int(idParts[1])
      return idParts
    except:
      return False

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
      print("{} has been added to the queue.".format(value))
    else:
      print("Queue is full!")
  
  def remove(self):
    if (self.array[self.start] != None):
      popped = self.array[self.start] 
      self.array[self.start] = None
      self.size -= 1
      # update start index
      if (self.start != (len(self.array) - 1)):
        self.start += 1
      else:
        self.start = 0

      return f"{popped[0]}: {popped[1]}.\nEnquiry answered."
    else:
      return "There are no enquiries."