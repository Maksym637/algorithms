def shellSort(myList: list) -> list:
    size = len(myList)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = myList[i]
            j = i
            while j >= gap and myList[j - gap] > anchor:
                myList[j] = myList[j - gap]
                j -= gap
            myList[j] = anchor
        gap = gap // 2

    return myList