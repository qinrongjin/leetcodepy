l = [1, 2, 3, 4]

l2 = l.copy()

l2.__delitem__(3)
l2.__delitem__(5)

print(l)

print(l2)