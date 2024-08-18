def saludar(idioma):
    def saludar_es():
        print('Hola')
    def saludar_en():
        print('Hi')
    func_idioma={
        'es': saludar_es,
        'en': saludar_en
    }
    return func_idioma[idioma]

el_saludo = saludar('es')
el_saludo()