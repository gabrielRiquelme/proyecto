def cuadrado(base,altura):
    area = base * altura
    return area

def circulo(radio):
    area = (radio ** 2) * 3.14
    return area

print("El area total es: ", cuadrado(10, 5))
print("El area total es: ", circulo(10))