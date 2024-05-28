class FabricaTelefonos():
    def __init__(self, marca, color): #Constructor#
        self.marca = marca
        self.color = color
        print("Objeto creado")

    def __str__(self): #Metodo que muestra que objeto es#
        return "El objeto es {}".format(self.marca)

    def __del__(self): #Metodo destructor#
        print("Objeto destruido")

telefono = FabricaTelefonos('Iphone','Blanco')
print(telefono.marca)
print(telefono.color)
print(telefono)
