arr = [15,38,7,23,14]
def occurs(number, array):
    for item in array:
        if item == number:
            return f'number {number} appears in the array'
    return f'number {number} does not appear in the array'
print(occurs(23,arr))
