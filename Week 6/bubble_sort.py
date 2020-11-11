def bubble_sort(numList):
  for i in range(len(numList)):
    for x in range (len(numList)-1):
      if (numList[x] > numList[x+1]):
        temp = numList[x+1]
        numList[x+1] = numList[x]
        numList[x] = temp

  return numList

print(bubble_sort([6,8,1,9,2,7]))