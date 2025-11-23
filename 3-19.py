array = [1,4,70,100,241,234,222]
number = int(input('Enter number: '))
def f(arr,num):
    greater = []
    for item in arr:
        if item > num:
            greater.append(item)
    return greater
print(f(array,number))