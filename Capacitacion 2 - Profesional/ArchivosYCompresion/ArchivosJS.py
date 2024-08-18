import json

with open(r'c:\Users\sofia\OneDrive\Documentos\Riki\proyecto\Capacitacion 2 - Profesional\ArchivosYCompresion\docu.txt') as file:
    data=json.load(file)
    print(data['cliente1'])
try:
    if(data['cliente']):
        print('Data encontrada')
except KeyError:
    print('Cliente no existente, ingrese otro cliente')
