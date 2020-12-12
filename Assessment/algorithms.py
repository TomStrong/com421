def insertion_sort(poiList):

  for i in range(1,len(poiList)):
    curVal = poiList[i]
    curIndex = i

    while (poiList[curIndex - 1].name > curVal.name):
      poiList[curIndex] = poiList[curIndex - 1]
      curIndex -= 1

    poiList[curIndex] = curVal

  return poiList