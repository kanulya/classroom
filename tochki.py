x1 = int(input("x1 "))
y1 = int(input("y1 "))
a = (x1,y1)
x2 = int(input("x2 "))
y2 = int(input("x3 "))
b = (x2,y2)
if x1 > 0 and x2 > 0 and y1 > 0 and y2 > 0:
	print(a, b, "lejat v odnoi chetverti")
elif x1 < 0 and x2 < 0 and y1 > 0 and y2 > 0:
	print(a, b, "lejat v odnoi chetverti")
elif x1 < 0 and x2 < 0 and y1 < 0 and y2 < 0:
	print(a, b, "lejat v odnoi chetverti")
elif x1 > 0 and x2 > 0 and y1 < 0 and y2 < 0:
	print(a, b, "lejat v odnoi chetverti")
else:
	print(a, b, "tochki lejat v raznyh chetvertyah")
