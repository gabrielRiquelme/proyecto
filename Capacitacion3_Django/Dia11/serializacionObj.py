import pickle
''' Codificar archivo

lista = ['Maria','Pedro','Jose','Paola']

fichero = open('lista','wb')

pickle.dump(lista, fichero)

fichero.close()
'''

fichero = open('lista','rb')

lista = pickle.load(fichero)

fichero.close()
print(lista)