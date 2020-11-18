def insertion_sort(numList):
  divider = 0
  for i in range(1,len(numList)):
    if (numList[i] > numList[divider]):
      divider += 1
    else:
      curIndex = i - 1
      while (numList[i] > numList[curIndex]):
        curIndex -= 1

      temp = numList[i]
      del numList[i]
      numList.insert(curIndex, temp)

  return numList

print(insertion_sort([6,8,1,9,2,7]))