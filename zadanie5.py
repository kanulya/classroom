dict_one = {'a':1, 'b':2, 'c':3}
dict_two = {'d':4, 'e':5, 'f':6}
dict_three = {'g':7, 'h':8, 'i':9}

def mergeDict12(dict_one, dict_two):
    for k, v in dict_two.items():
        if dict_one.get(k):
            dict_one[k] = [dict_one[k], v]
        else:
            dict_one[k] = v
    return dict_one

dict_four = mergeDict12(dict_one, dict_two)

def mergeDict3(dict_four, dict_three):
    for k, v in dict_three.items():
        if dict_four.get(k):
            dict_four[k] = [dict_four[k], v]
        else:
            dict_four[k] = v
    return dict_four

dict_four = mergeDict3(dict_four, dict_three)

print(dict_four)

