class Coche:
    def __init__(self,marca,kilometros,anio):
        self.__marca = marca #Encapsulamiento, para que se pueda modificar por fuera.#
        self.__kilometros = kilometros
        self.__anio = anio
        self.ruedas = 4
        print(f'Se ha creado un auto{self.__marca},con {self.__kilometros} kilometros')

    def arrancar(self,arrancamos):
        self.enmarcha = arrancamos
        if(self.enmarcha):
            return 'El auto esta encendido.'
        else:
            return 'El auto esta apagado.'


    def __str__(self):
        return 'El auto es un {}, tiene {}, y es del año {}'.format(self.__marca,self.__kilometros,self.__anio)

miAuto = Coche('Audi',200,1995)
print(str(miAuto))
print(miAuto.arrancar(False))

miAuto2 = Coche('Audi',500,1990)
miAuto2.marca = 'VW'
print(str(miAuto2))


