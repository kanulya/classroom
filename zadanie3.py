# Напишите функцию которая принимает два аргумента (числа), умножает их друг на друга,
# и возвращает функцию, которая также берет два аргумента (числа),
# и возвращает результат умножения аргументов внешней функции плюс результат деления
# аргументов внутренней функции.
# Подсказка: (outer_arg1 * outer_arg2) + (inner_arg1 / inner_arg2)

def multi():
    global outer_arg1, outer_arg2
    outer_arg1 = int(input())
    outer_arg2 = int(input())
    return outer_arg1 * outer_arg2
print(multi())
def multi():
    inner_arg1 = int(input())
    inner_arg2 = int(input())
    return outer_arg1 * outer_arg2 + (inner_arg1 / inner_arg2)
print(multi())