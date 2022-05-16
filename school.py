school = {}
school['1a'] = 39
school['1b'] = 41
school['2a'] = 40
school['2b'] = 39
school['3a'] = 38
school['3b'] = 37
school['4a'] = 31
school['4b'] = 35
school['4c'] = 28
print(school)
school['3b'] = 31
kl = {'1c': 30}
school.update(kl)
school.pop('4c')
print(school)
vsego = sum(school.values())
print(vsego)
