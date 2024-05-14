candidato = input('Bienvenido al sistema electoral, porfavor para votar a su candidato ingrese la A para votar al partido ROJO, B para el partido VERDE y C para el partido AZUL: ')

if candidato.upper() == "A":
    print('Usted a votado a la lista ROJA')
elif candidato.upper() == "B":
    print('Usted a votado a la lista VERDE')
elif candidato.upper() == "C":
    print('Usted a votado a la lista AZUL')
else:
    print("Opcion incorrecta")