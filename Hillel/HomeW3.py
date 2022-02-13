x = int(input("Введите 4-х значное число: "))
if x <= 999 or x >= 10000:
    print("Вы ввели не верное число!")
    x = False

if x >=1000 or x <=9999:
    a = x % 1000
    b = x // 1000
    print(b)

    c = a % 100
    b = a // 100
    print(b)

    a = c % 10
    b = c // 10
    print(b)

    c = a % 1
    b = a // 1
    print(b)


