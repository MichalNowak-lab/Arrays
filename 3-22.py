import random
arr = [1,2,7676,32,7,234,122]
def rand_elem(array):
    return array[random.randint(0,len(arr)-1)]
print(rand_elem(arr))