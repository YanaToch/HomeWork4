lst = [0, 10, 87, 24, 0, 58, 97, 0, 25]
for i in range(len(lst)):
    if lst[i] == 0:
        lst.extend([0])
        del(lst[i])
print(lst)
