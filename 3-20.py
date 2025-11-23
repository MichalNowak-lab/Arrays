arr = [7,9,2,4,5,6]
def evenOdd(arr):
    sort_arr = []
    for i in range(2):
        for item in arr:
            if i == 0 and item%2==0:
                sort_arr.append(item)
            elif i == 1 and item%2!=0:
                sort_arr.append(item)
    return sort_arr
print(evenOdd(arr))