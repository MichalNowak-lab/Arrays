tuple = (50,20,40,50,30,50)
arr = []
for item in tuple:
    if item not in arr:
        print(f'Value: {item}')
        print(f'Number of occurrences: {tuple.count(item)}')
    arr.append(item)