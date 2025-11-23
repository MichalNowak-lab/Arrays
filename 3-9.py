array1 = [5,3,1]
array2 = [5,3,1]

def compare(array1, array2):
    lenght = len(array1)==len(array2)
    elements = True
    if not lenght:
        return 'Arrays are not the same'
    else:
        for i in range(len(array1)):
            if array1[i]!=array2[i]:
                return 'Arrays are not the same'
    return 'Arrays are the same'
print('Array1:',*array1)
print('Array1:',*array2)
print('Comparison:',compare(array1,array2))