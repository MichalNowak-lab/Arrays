import matplotlib.pyplot as plt

x = []
y = []

for n in range(-100,101):
   x = x + [n]

for n in x:
   y = y+[n**2-3]

plt.plot(x, y)

plt.show()