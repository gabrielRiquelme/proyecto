import pickle

dic1 = {'Iphone':'15 PRO','Xiaomi':'POCO 13','Samsung':'S24 Ultra'}

fichero = open('diccionariSerializado','wb')
pickle.dump(dic1,fichero)
fichero.close()
del(fichero)

