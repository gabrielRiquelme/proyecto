class Libro():
    def __init__(self, nombre,autor,paginas):
        self.nombre = nombre
        self.autor = autor
        self.paginas = paginas

    def describir(self):
        print(f'Hola desde describir, {self.nombre}')

    def __str__(self):
        return f'{self.nombre} escrito por {self.autor}'
    
    def __len__(self):
        return self.paginas
    
libro1 = Libro('Estoicismo', 'Juan Riquelme', 450)

print(len(libro1))