RandomNumber = int(input("Введите произвольное число: "))
BorderNumber = int(input("Введите пограничное число: "))

if RandomNumber < BorderNumber:
    print("Произвольное число меньше пограничного")
elif RandomNumber/3 >= BorderNumber:
    print("Произвольное число больше пограничного в 3 раза")
else:
    print("Произвольное число больше пограничного")




