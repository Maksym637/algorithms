def bubbleSort2(myList: list) -> list:
    for i in range(len(myList) - 1, 0, -1):
        for j in range(i):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
    return myList