# Weekly expenses for different categories
# [Food, Transport, Utilities]

monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food = 0
transport = 0
utilities = 0
week1 = 0
week2 = 0
week3 = 0
week4 = 0
week_counter = 1
for row in monthly_expenses:

    i=1
    for type in row:
        if i == 1:
            food+=type
        elif i == 2:
            transport+=type
        elif i == 3:
            utilities+=type
        i+=1
        if week_counter == 1:
            week1 += type
        if week_counter == 2:
            week2 += type
        if week_counter == 3:
            week3 += type
        if week_counter == 4:
            week4 += type
    week_counter += 1
total = week1+week2+week3+week4
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',transport)
print('Utilities:',utilities)
print('Week 1:',week1)
print('Week 2:',week2)
print('Week 3:',week3)
print('Week 4:',week4)
print('---------------')
print('TOTAL:',total)