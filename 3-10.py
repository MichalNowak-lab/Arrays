array1 = [4,36,12,28,9,44,5]
array2 = [5,1,36]
i = 0
for item in array1:
    appears = False
    for item2 in array2:
        if item == item2:
            appears = True
    if appears == False:
        print(item, end=' ')