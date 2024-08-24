class Coche:
    def __init__(self,marca,kilometros,anio,color):
        self.__marca = marca #Encapsulamiento, para que se pueda modificar por fuera.#
        self.__kilometros = kilometros
        self.__anio = anio
        self.color = color

    def arrancar(self,arrancamos):
        self.enmarcha = arrancamos
        if(self.enmarcha):
            return 'El auto esta encendido.'
        else:
            return 'El auto esta apagado.'
    
    def __str__(self):
        return 'El auto es un {}, tiene {} kilometros, es del año {} y es de color {}'.format(self.__marca,self.__kilometros,self.__anio,self.color)
        
auto = Coche('VW',100,2010,'Negro')
print(str(auto))
print(auto.arrancar(True))