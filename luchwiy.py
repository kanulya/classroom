john = ["algebra", 100, "biologia", 84, "fizika", 61, "himia", 78, "english", 88, "geometria", 89, "informatika", 98]
james = ["algebra", 98, "biologia", 90, "fizika", 88, "himia", 67, "english", 90, "geometria", 94, "informatika", 96 ]
kate = ["algebra", 99,"biologia", 95,"fizika", 83,"himia",68,"english",97, "geometria", 96, "informatika", 98]
jod = dict(zip(john[::2], john[1::2]))
print("John: ", jod)
s1 = sum(jod.values())//7
print("John: ", s1, " points")
jad = dict(zip(james[::2], james[1::2]))
print("James: ", jad)
s2 = sum(jad.values())//7
print("James: ", s2, " points")
kad = dict(zip(kate[::2], kate[1::2]))
print("Kate: ", kad)
s3 = sum(kad.values())//7
print("Kate: ", s3, " points")
if s1 > s2 and s1 > s3:
    print("John is the best student")
elif s2 > s1 and s2 > s3:
    print('James is the best student')
else:
    print("Kate is the best student")
