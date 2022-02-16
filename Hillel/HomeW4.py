first = float(input("Введите 1-е число:  "))
second = float(input("Введите 2-е число:  "))
operation = input("Введите действие (+,-,*,/,**):  ")
if operation == '+':
    print(first + second)
elif operation == '-':
    print(first - second)
elif operation == '*':
    print(first * second)
elif operation == '/' and second != 0:
    print(first / second)
elif operation == '/' and second == 0:
    print('Делить на ноль нельзя!')
elif operation == "**":
    print(first ** second)

