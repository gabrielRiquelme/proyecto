class Gelatina:
    def __init__(self,sabor,color,tamanio):
        self.sabor = sabor
        self.color = color
        self.tamanio = tamanio

    def imprimir(self):
        print(f'La gelatina es de {self.sabor}')
        print(f'La gelatina es de color {self.color}')
        print(f'La gelatina es de tamaño {self.tamanio}')

postre1=Gelatina('Frutilla','Rojo','2Litros')

postre2=Gelatina('Naranja','Naranja','1litro')

postre1.imprimir()
print('')
postre2.imprimir()