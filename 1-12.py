categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
price = max(expenses)
index_max = expenses.index(price)
print(categories[index_max])