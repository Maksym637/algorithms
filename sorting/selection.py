def selectionSort(myList: list) -> list:
    for i in range(len(myList) - 1):
        minIndex = i
        for j in range(i + 1, len(myList)):
            if myList[j] < myList[minIndex]:
                minIndex = j
        if minIndex != i:
            myList[i], myList[minIndex] = myList[minIndex], myList[i]
    return myList