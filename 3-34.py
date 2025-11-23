
def identity_matrix(n):
    identity = []
    for i in range(n):
        row = [0 for r in range(n)]
        row[i] = row[i]+1
        identity.append(row)
    return identity
for row in identity_matrix(3):
    for value in row:
        print(value, end=' ')
    print()
print('\n')
for row in identity_matrix(5):
    for value in row:
        print(value, end=' ')
    print()
print('\n')
for row in identity_matrix(8):
    for value in row:
        print(value, end=' ')
    print()