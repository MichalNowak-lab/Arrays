array = [2,3,2,5,8,1,9,8]
unique_numbers = []
for item in array:
    if array.count(item)<2:
        unique_numbers.append(item)
print(unique_numbers)
