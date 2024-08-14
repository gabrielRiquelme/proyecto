class Libro():
    def __init__(self, nombre,autor,paginas):
        self.nombre = nombre
        self.autor = autor
        self.paginas = paginas

    def __str__(self): #Muestra mensaje al llamar al objeto#
        return f'{self.nombre} escrito por {self.autor}'
    
    def __len__(self): #Muestra contenido de atributos. EJ de paginas = 450#
        return self.paginas
    
    def __del__(self): #Muestra mensaje de que se elimino un objeto#
        print('Se ha eliminado un libro...')

    
libro1 = Libro('Estoicismo', 'Juan Riquelme', 450)


del libro1


