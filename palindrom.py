words = ['Anna', 'Civic', 'Kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
nwords = [x.upper() for x in words]
for i in nwords:
    if i == i[::-1]:
        print(i, " :palindrom", end=', ')
    else:
        print(i, " :ne palindrom", end=', ')
