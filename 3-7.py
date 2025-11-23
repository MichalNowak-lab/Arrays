array = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
longest = len(array[0])
temp = 0
for item in array:
    if len(item)>=longest:
        longest = len(item)
        temp = item
print(temp)
