#Modificacion de metodos desde una clase hija hacia padre y la modificacion de metodos de clases heredadas #
class Marino():
    def hablar(self):
        print('Hola...')

class Pulpo(Marino):
    def hablar(self):
        print("Soy un pulpo")

class Foca(Marino):
    def hablar(self,msg):
        self._msg = msg
        print(self.msg)

pul = Pulpo()
foca = Foca()

pul.hablar()
foca.hablar('Hola soy una foca')
        