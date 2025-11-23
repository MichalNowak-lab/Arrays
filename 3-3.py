array = [8,2,5,1,9]
def squared(arr):
    for i in range(len(arr)):
        arr[i] = arr[i]**2
    return arr
print(squared(array))