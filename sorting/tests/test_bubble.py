from bubble1 import bubbleSort1
from bubble2 import bubbleSort2

arr1 = [-100, -200, 0, 10, 3, 5, 6, 2, 2, 2, 1]
arr2 = [1, 2, 3, 4, 6, 5]
arr3 = [11, 3, 7, 5, 2]

def test_bubbleSort1():
    assert bubbleSort1(arr1) == [-200, -100, 0, 1, 2, 2, 2, 3, 5, 6, 10]
    assert bubbleSort1(arr2) == [1, 2, 3, 4, 5, 6]
    assert bubbleSort1(arr3) == [2, 3, 5, 7, 11]

def test_bubbleSort2():
    assert bubbleSort2(arr1) == [-200, -100, 0, 1, 2, 2, 2, 3, 5, 6, 10]
    assert bubbleSort2(arr2) == [1, 2, 3, 4, 5, 6]
    assert bubbleSort2(arr3) == [2, 3, 5, 7, 11]