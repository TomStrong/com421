import datastructures as ds

def addPOI(): # ---TASK 1---

  name = input("Enter the POI name: ")
  if (ds.POI.validateName(name)):
    pType = input("Enter the POI type: ")
    desc = input("Enter the POI description: ")
    table.add(ds.POI(name, pType, desc))
  else:
    print("A name must contain letters.")

  return True

def idSearch(): # ---TASK 2---

  pID = input("Enter the POI ID: ")
  print(table.lookup(pID=pID))

  return True

def showAll(): # ---TASK 3---

  print(table)

  return True

def nameSearch(): # ---TASK 4---

  name = input("Enter the POI name: ")
  for item in table.lookup(name=name):
    print(item)

  return True

def deletePOI(): # ---TASK 5---

  pID = input("Enter the POI ID: ")
  table.delete(pID)

  return True

def makeEnquiry(): # ---TASK 6---

  pID = input("Enter the POI ID: ")
  search = table.lookup(pID=pID)
  if (search == "That POI does not exist."):
    print(search)
    return True

  print(search)
  enquiry = input("\nEnter an enquiry for the POI listed above.\n>> ")
  enquiryTuple = (pID, enquiry)
  enquiries.add(enquiryTuple)

  return True

def answerEnquiry(): # ---TASK 6---

  print(enquiries.remove())

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
  global enquiries
  enquiries = ds.Queue(20)

  options = {
    1: addPOI,
    2: idSearch,
    3: showAll,
    4: nameSearch,
    5: deletePOI,
    6: makeEnquiry,
    7: answerEnquiry,
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
    print("6: Make an enquiry")
    print("7: Answer enquiry")
    print("\n9: Exit")
    selection = int(input(">> "))
    print()
    if (selection != 1 and selection != 7 and selection != 9):
      if (table.count > 0):
        running = options.get(selection, inval)()
      else:
        print("No POIs are stored.")
    else:
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