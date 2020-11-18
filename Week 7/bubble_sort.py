def bubble_sort(numList):
  for i in range(len(numList)):
    temp = None
    for x in range(len(numList)-1):
      if (numList[x] > numList[x+1]):
        temp = numList[x+1]
        numList[x+1] = numList[x]
        numList[x] = temp

      if (x == len(numList) - 2 and temp == None):
        return numList

  return numList

print(bubble_sort([1,6,8,9,2,7]))