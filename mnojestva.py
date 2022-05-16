# 1.Объединить 2 множества
months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
# 2.Добавить месяц, которого нету во множестве
# 3.Перебрать элементы множества
# 4.Вам даны 2 множества, узнать какие элементы пересекаются между ними.

m = months_a.union(months_b)
print(m)
m.add("Dec")
print(m)
for i in m:
    print(i)


x = {1, 2, 3}
y = {4, 3, 6}

z = x.intersection(y)
print(z)
