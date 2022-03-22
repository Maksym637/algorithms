from insertion import insertionSort

arr1 = [-100, -200, 0, 10, 3, 5, 6, 2, 2, 2, 1]
arr2 = [1, 2, 3, 4, 6, 5]
arr3 = [11, 3, 7, 5, 2]
arr4 = [12, 11, 13, 5, 6, 7]
arr5 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def test_insertionSort():
    assert insertionSort(arr1) == [-200, -100, 0, 1, 2, 2, 2, 3, 5, 6, 10]
    assert insertionSort(arr2) == [1, 2, 3, 4, 5, 6]
    assert insertionSort(arr3) == [2, 3, 5, 7, 11]
    assert insertionSort(arr4) == [5, 6, 7, 11, 12, 13]
    assert insertionSort(arr5) == [1, 2, 3, 4, 5, 6, 7, 8, 9]