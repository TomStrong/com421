import math

def binary_search(searchVal):
  numbers = [i*i for i in range(1,101)]
  top = len(numbers)-1
  bot = 0
  
  while True:
    searchIndex = math.floor((top + bot) / 2)

    if (numbers[searchIndex] == searchVal):
      return "Index: {}".format(searchIndex)
    elif (top == bot or top < 0):
      return "Not in list."
    elif (numbers[searchIndex] > searchVal):
      top = searchIndex - 1
    elif (numbers[searchIndex] < searchVal):
      bot = searchIndex + 1

def run():
  search = int(input("Number: "))
  print(binary_search(search))

run()