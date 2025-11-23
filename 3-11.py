array1 = [12,2,333,112,33,2,1,666,545,76]
array2 = [777,444,666,555,222,11]
array3 = [444,42124,22,1,6545,3,2]
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubblesort(array1))
print(bubblesort(array2))
print(bubblesort(array3))