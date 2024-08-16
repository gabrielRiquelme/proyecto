class Libro():
    def __init__(self,nombre,autor,pags):
        self.nombre = nombre
        self.autor = autor
        self.pags = pags

    def decribir(self):
        print(f'Hola desde describir',{self.nombre})

    def __str__(self):
        return f'{self.nombre} escrito por {self.autor}'

libro1 = Libro('Estoicismo','JuanR',600)

print(libro1)