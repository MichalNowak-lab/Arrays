import MyArrays
array = [7,3,8,5,2]
numbers = ''

for item in array:
    numbers+=f',{item}'
numbers = numbers[1:]


def maxNumMinNum(arr):
    n = len(arr)
    arra = []
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    arra.append(arr[0])
    arra.append(arr[-1])
    return arra


def numAsString(arr):
    strin = ''
    for item in arr:
        strin+=f'-{item}'
    return strin[1:]
print(f'Numbers: {array}')
print(f'Second largest nuber: {MyArrays.secondLargest(array)}')
print(f'Median: {MyArrays.median(array)}')
print(f'Smallest and largest number: {maxNumMinNum(array)}')
print(f'Numbers as string: {numAsString(array)}')