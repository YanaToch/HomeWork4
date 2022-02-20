lst = [125, 354, 657, 98, 51, 25, 41, 10]
print(lst)
if not lst:
    print([])
else:
    a = lst[-1]
    lst.insert(0, a)
    del(lst[-1])
    print(lst)




