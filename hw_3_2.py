list_1 = [12, 3, 4, 10]
if len(list_1) > 1:
    list_1.insert(0, list_1[-1])
    list_1.pop(-1)
print(list_1)

list_2 = [1]
if len(list_2) > 1:
    list_2.insert(0, list_2[-1])
    list_2.pop(-1)
print(list_2)

list_3 = []
if len(list_3) > 1:
    list_3.insert(0, list_3[-1])
    list_3.pop(-1)
print(list_3)

list_4 = [12, 3, 4, 10, 8]
if len(list_4) > 1:
    list_4.insert(0, list_4[-1])
    list_4.pop(-1)
print(list_4)
