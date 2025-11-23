array = [-15, 8, -31, 47, -2, 19]
def maximum(arr):
    temp = 0
    maxi = arr[0]
    for item in arr:
        if item >= maxi:
            maxi = item
    return maxi

def minimum(arr):
    temp = 0
    mini = arr[0]
    for item in arr:
        if item <= mini:
            mini = item
    return mini
print(maximum(array))
print(minimum(array))