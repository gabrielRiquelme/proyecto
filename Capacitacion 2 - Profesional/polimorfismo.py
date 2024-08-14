class Perro():
    def avanzar(self):
        print('Tengo 4 patas')


class Perico():
    def avanzar(self):
        print('Volar')


def mover(animal):
    animal.avanzar()

print('aca no se ejecuta polimorfismo')
perro = Perro()
perro.avanzar()
perico = Perico()
perico.avanzar()

print('*'*20,'Polimorfismo','*'*20)
mover(perro)
mover(perico)
