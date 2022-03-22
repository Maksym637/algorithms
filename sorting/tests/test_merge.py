from merge import mergeSort

arr1 = [-100, -200, 0, 10, 3, 5, 6, 2, 2, 2, 1]
arr2 = [1, 2, 3, 4, 6, 5]
arr3 = [11, 3, 7, 5, 2]
arr4 = [5, 9, 1, 2, 4, 8, 6, 3, 7]
arr5 = [1, 10, 10, 10, 2, 2, 2]

def test_mergeSort():
    mergeSort(arr1)
    mergeSort(arr2)
    mergeSort(arr3)
    mergeSort(arr4)
    mergeSort(arr5)
    assert arr1 == [-200, -100, 0, 1, 2, 2, 2, 3, 5, 6, 10]
    assert arr2 == [1, 2, 3, 4, 5, 6]
    assert arr3 == [2, 3, 5, 7, 11]
    assert arr4 == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert arr5 == [1, 2, 2, 2, 10, 10, 10]