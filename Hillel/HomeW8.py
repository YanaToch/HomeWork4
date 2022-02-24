lst = [72, 25, 87, 55, 22, 12, 8, 11, 10]
print(lst)
lst_sum = 0

if not lst:
    print('0')
else:
    for el in range(len(lst)):
        if lst[el] % 2 == 0:
            print(lst[el], end=" ")
            lst_sum += lst[el]
    print(lst_sum * lst[-1])

