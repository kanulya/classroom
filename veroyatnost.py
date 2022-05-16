
from random import random
m = 1000
c = 0
for i in range(1000):
    if int(random()*100) % 2 == 0:
        c += 1
print("%.2f%%" % (c / m * 100))
