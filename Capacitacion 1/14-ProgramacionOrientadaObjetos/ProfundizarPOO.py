# *colores = tupla / **modelos = diccionario#
class FabricaTelefonos():
    def __init__(self , marca , *colores , **modelos): #Constructor / Atributos#
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos("Iphone","Negro" , "Blanco", m1 = 500, m2 = 1000)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
telefono.memoria = 512
print(telefono.memoria) #Atributos temporales.#