class Persona():
    def __init__(self):
        pass

    def saltar(self):
        print('Estoy saltando...')

    @classmethod
    def correr(cls):
        print('Estoy corriendo...')

    @staticmethod
    def nadar():
        print('Estoy nadando...')


juan = Persona()

juan.nadar()