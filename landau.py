k = int(input('Обхват по бюсту, см '))
m = int(input('Обхват по бёдрам, см '))
n = int(input('Обхват по талии, см '))
t = int(input('Рост, см '))
p = int(input('Вес, кг '))
l = (k*m*t)/(n**2*p)
print(l)
