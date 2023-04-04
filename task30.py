# Заполните массив элементами арифметической прогрессии. 
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

def GetValueByUser(Num):
    while True:
        getnum = input(Num)
        if getnum.isdigit():
            return getnum
        
def GetProgression(FE, D, NE):
    arr = list()
    for i in range(NE):
        an = FE + ( i - 1 ) * D
        arr.append(an)
    return arr
FirstElement = int(GetValueByUser('Введите первый элемент прогрессии: '))
Difference = int(GetValueByUser('Введите разность: '))
NumberOfElements = int(GetValueByUser('Введите количество элементов прогрессии: '))
print('Арифметическая прогрессия: ', GetProgression(FirstElement, Difference, NumberOfElements))