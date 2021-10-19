Stroka = input("Введите произвольную строку: ")
Dlina = len(Stroka)
Cimvol = False
Schet = 1

for i in Stroka:
    if i == 'с':
        Cimvol = True

    if Schet == 3:
        Schet += 1
        continue
        print(i, end="")
        Schet += 1

    if Schet == Dlina:
        break

    print(i, end="")
    Schet += 1
if Cimvol == True:
    print("\nПрисутствует буква С")