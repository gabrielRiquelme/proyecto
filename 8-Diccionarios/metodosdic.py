dic = {1:2 , 2:3 , 3:4}
dic2 = {4:5 , 6:7}

print(dic)

#dic.pop(3) elimina clave valor que contenga la llave 3

#print(dic)

#dic.clear() elimina todo del dic

#print(dic)

print(dic.get(2)) #Muestra valor de llave 2.

print(dic)

dic.setdefault(4 , 5) #agregar key y valor

print(dic)

dic.update(dic2) # Junta ambos diccionarios en uno.

print(dic)

dic.copy()
print(dic)
