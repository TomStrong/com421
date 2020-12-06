def insertion_sort(poiList):
  divider = 0
  for i in range(1,len(poiList)):
    if (poiList[i].name > poiList[divider].name):
      divider += 1
    else:
      curIndex = i - 1
      while (poiList[i].name < poiList[curIndex-1].name):
        curIndex -= 1

      temp = poiList[i]
      del poiList[i]
      poiList.insert(curIndex, temp)

  return poiList