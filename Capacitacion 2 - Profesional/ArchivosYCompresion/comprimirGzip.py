import gzip

with open('docu.txt','rb') as file:
    with gzip.open('fichero.txt.gz', 'wb') as fichero:
        fichero.writelines(file)