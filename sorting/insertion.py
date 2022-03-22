def insertionSort(myList: list) -> list:
    for i in range(1, len(myList)):
        curNum = myList[i]
        k = 0
        for j in range(i - 1, -2, -1):
            k = j
            if myList[j] > curNum:
                myList[j + 1] = myList[j]
            else:
                break
        myList[k + 1] = curNum
    return myList