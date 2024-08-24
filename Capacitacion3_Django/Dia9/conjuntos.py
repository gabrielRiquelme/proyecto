i = set()
i={1,2,3,4}
b = i.copy()
i.add(1)
i.add(2)
b.discard(3)
i.add(3)
i.clear()
b.clear()
print(i,b)

