#array = [1,32,3,2,3,2]

def secondLargest(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[-2]

def differenceMinMax(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    difference = arr[-1]-arr[0]
    return difference

def median(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    if len(arr)%2 == 0:
        mediana = (arr[len(arr)//2]+arr[len(arr)//2+1])/2
        return mediana
    else:
        return arr[len(arr)//2]
#print(median(array))
#print(differenceMinMax(array))
#print(secondLargest(array))