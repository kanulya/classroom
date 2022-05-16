my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
a, b, c = 0, 0, 0
for i, j in my_dict.items():
    max1 = max(my_dict.values())
    if j == max1:
        if a > 0:
            b = j
        elif b > 0:
            c = j
        else:
            a = j
        my_dict.pop(i)
        break
for i, j in my_dict.items():
    max1 = max(my_dict.values())
    if j == max1:
        if a > 0:
            b = j
        elif b > 0:
            c = j
        else:
            a = j
        my_dict.pop(i)
        break
for i, j in my_dict.items():
    max1 = max(my_dict.values())
    if j == max1:
        if a > 0:
            c = j
        elif b > 0:
            b = j
        else:
            a = j
        my_dict.pop(i)
        break

print(my_dict, a, b, c)
