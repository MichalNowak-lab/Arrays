arr1 = [1,2,3,4,5]
arr2 = [1,2,3,4,5,6,7,8,9,10]
def is_subset(arr1, arr2):
    for element in arr1:
        if element not in arr2:
            return False
    return True
print(is_subset(arr1,arr2))