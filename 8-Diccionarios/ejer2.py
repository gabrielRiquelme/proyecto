jugadores = {  1 : "Casillas", 15 : "Ramos", 3 : "Pique", 5 : "Puyol", 11 : "Capdevila", 14 : "Xabi Alonso", 16 : "Busquets", 8 : "Xavi Hernandez",18 : "Pedrito", 6 : "Iniesta", 7 : "Villa"}

num = int(input('Ingrese un numero que coincida con el dorsal de un jugador de la seleccion española de 2010: '))

if num in jugadores:
    print(jugadores[num])
else:
    print('Jugador no encontrado')