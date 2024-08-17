def decorador(funcionComun):
    def funcionDecoradora(*args,**kwargs):
        print('Mi primer funcion decoradora')
    return funcionDecoradora

@decorador
def funcionComun():
    print('Mi funcion comun')

funcionComun()