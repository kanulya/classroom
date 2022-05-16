
n=int(input(''' Выберите действие:
1. Добавить новый город
2. Отобразить список городов
3. Заменить город
4. Удалить город
5. Выход
'''))

list1=['Ош','Бишкек','Каракол', 'Токмок']
while True:
# vibor 1
    if n==1:
        name1=input('Введите название города: ' )
        if name1.isdigit():
            print('Некорректное название!')
        elif name1 in list1:
            print('Такой город уже есть! ', name1)
        else:
            list1.append(name1)
            print('Город добавлен!')
    n=int(input(''' Выберите действие:
    1. Добавить новый город
    2. Отобразить список городов
    3. Заменить город
    4. Удалить город
    5. Посетить следующий город
    6. Выход
    '''))
# vibor 2
    if n==2:
        for i in range(len(list1)):
            print (i+1,'Список городов.', list1[i])
# vibor 3
    if n==3:
        a = input('Текущий город: ' )
        b = input('Новый город: ')
        if a.isdigit() or b.isascii():
            print('Некорректное название!')
        if a in list1:
            if a==b:
                print('Такой город уже есть!')
            else:
                list1.remove(a)
                list1.append(b)
                print('Город заменен.')
        else:
            print('Текущий город отсутствует.')
# vibor 4
    if n==4:
        c= input("Введите название города: ")
        if c.isdigit() :
            print('Некорректное название!')
        if c in list1:
            list1.remove(c)
            print('Город удален!')
        else:
            print('Текущий город отсутствует.')
# vibor 5
    if n==5:
        print('Программа завершила работу.')
        break
