#Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)

Array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print(Array)
Min = int(input("Введите минимум: "))
Max = int(input("Введите максимум: "))

ArrayOfIndex = list()
for i in range(len(Array)):
    if Min < Array [i] < Max:
        ArrayOfIndex.append(i)
print('Индексы элементов: ')
print(ArrayOfIndex)