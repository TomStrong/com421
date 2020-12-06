import datastructures as ds

def addPOI(): # ---TASK 1---

  name = input("Enter the POI name: ")
  pType = input("Enter the POI type: ")
  desc = input("Enter the POI description: ")
  table.add(ds.POI(name, pType, desc))

  return True

def idSearch(): # ---TASK 2---

  pID = input("Enter the POI ID: ")
  table.lookup(id=pID)

  return True

def showAll(): # ---TASK 3---

  print(table)

  return True

def nameSearch(): # ---TASK 4---

  name = input("Enter the POI name: ")
  table.lookup(name=name)

  return True

def deletePOI(): # ---TASK 5---

  pID = input("Enter the POI ID: ")
  table.delete(pID)

  return True

def inval():

  print("Invalid entry.")

  return True

def end():

  print("Closing...")

  return False



# ---MAIN PROG---
def main():
  global table
  table = ds.HashTable()

  options = {
    1: addPOI,
    2: idSearch,
    3: showAll,
    4: nameSearch,
    5: deletePOI,
    9: end
  }

  running = True

  while running:
    print("Select an action:")
    print("1: Add a new point of interest.")
    print("2: Search POIs by ID")
    print("3: Display all POIs")
    print("4: Search POIs by name")
    print("5: Delete a POI")
    print("\n9: Exit")
    selection = int(input(">> "))
    print()
    running = options.get(selection, inval)()
    print() 



if __name__ == '__main__':
    main()






"""
#####################
### ---TESTING--- ###
#####################

# add POIs ---TASK 1---
item1 = ds.POI("KFC", "Fast food", "Serves chicken")
item2 = ds.POI("McDonalds", "Fast food", "Serves burgers and chips")
item3 = ds.POI("Eifel Tower", "Landmark", "Big tower thing in Paris")
item4 = ds.POI("KFC", "Fast food", "Serves more chicken")
item5 = ds.POI("Taco Bell", "Fast food", "Serves tacos")
item6 = ds.POI("Pizza Hut", "Fast food", "Serves pizza")
item7 = ds.POI("Burger King", "Fast food", "Serves better burgers than maccers")
item8 = ds.POI("A", "Fast food", "Serves better burgers than maccers")
item9 = ds.POI("ZZZZZ", "Fast food", "Serves better burgers than maccers")
item10 = ds.POI("KEZ", "Test", "Test")

table.add(ds.POI("KEZ", "Test", "Test"))
table.add(ds.POI("KFC", "Fast food", "Serves chicken"))
table.add(ds.POI("ABC", "Test", "Test"))
table.add(ds.POI("DGE", "Test", "Test"))
table.add(ds.POI("ACD", "Test", "Test"))
table.add(ds.POI("ABC", "Test", "Test"))
table.add(ds.POI("ACE", "Test", "Test"))
table.add(ds.POI("KGP", "Test", "Test"))
table.add(ds.POI("KEQ", "Test", "Test"))
table.add(ds.POI("KFC", "Test", "Test"))
table.add(ds.POI("DGE", "Test", "Test"))
table.add(ds.POI("DBQ", "Test", "Test"))
table.add(ds.POI("DNA", "Test", "Test"))
table.add(ds.POI("ACD", "Test", "Test"))
table.add(ds.POI("ACE", "Test", "Test"))
table.add(ds.POI("KEZ", "Test", "Test"))


# display all POIs sorted by name ---TASK 3---
print(table)
"""