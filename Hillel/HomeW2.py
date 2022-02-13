x = int(input("Введите 5-ти значное число: "))

if x <= 9999 or x >= 100000:
    print("Вы ввели не верное число!")

if x >= 10000 or x <= 99999:
    y = 0
    c = x % 10
    x = x // 10
    y = y * 10
    y = y + c

    d = x % 10
    x = x // 10
    z = y * 10
    z = z + d

    e = x % 10
    x = x // 10
    w = z * 10
    w = w + e

    f = x % 10
    x = x // 10
    a = w * 10
    a = a + f

    g = x % 10
    x = x // 10
    b = a * 10
    b = b + g
    print(b)
