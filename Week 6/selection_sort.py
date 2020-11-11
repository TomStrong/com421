def selection_sort(numList):
  for i in range(len(numList)-1):
    minIndex = i

    for x in range(len(numList)-i):
      curIndex = x + i
      if (numList[minIndex] > numList[curIndex]):
        minIndex = curIndex

    temp = numList[minIndex]
    numList[minIndex] = numList[i]
    numList[i] = temp

  return numList

print(selection_sort([6,8,1,9,2,7]))