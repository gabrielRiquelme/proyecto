while True:
    try:    
        edad = int(input('Ingrese su edad: '))
        print('Tu edad es: ', edad)
        break
    except:
        print('Ingresaste un valor erroneo.')
    finally:
        print('Edad registrada correctamente') #siempre se ejecuta, OJO#

