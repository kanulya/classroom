x = int(input("x "))
y = int(input("y "))
a = (x,y)
if x > 0 and y > 0:
	print(a, "lejit v 1 chetverti")
elif x < 0 and y > 0:
	print(a, "lejit vo 2 chetverti")
elif x < 0 and y < 0:
	print(a, "lejit v 3 chetverti")
elif x > 0 and y < 0:
	print(a, "lejit v 4 chetverti")

