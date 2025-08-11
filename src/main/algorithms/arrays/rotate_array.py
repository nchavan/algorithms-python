def rotate_array(arr, k):
    n = len(arr)
    arrFinal = [];
    for i in range(n):
        index = i + k
        if (index >= n):
            index = index - n - 1;
        arrFinal.insert(index, arr[index])

    return arrFinal
