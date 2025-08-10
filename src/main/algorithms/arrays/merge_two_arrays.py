def mergeArrays(arr1, arr2):

    if arr1 is None or arr2 is None:
        return []

    arrayFinal = arr1 + arr2
    arrayFinal.sort()
    return arrayFinal
