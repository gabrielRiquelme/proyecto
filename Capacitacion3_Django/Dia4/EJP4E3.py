divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
divisa_usuario = input("Introduce el nombre de la divisa (Euro, Dollar, Yen): ")

if divisa_usuario in divisas:
    print(f"El símbolo de {divisa_usuario} es {divisas[divisa_usuario]}.")
else:
    print("La divisa introducida no se encuentra en el diccionario.")
