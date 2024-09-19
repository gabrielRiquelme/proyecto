from zipfile import *

with ZipFile('1808_3633628-1726407756474.zip', 'r') as myzip:
    myzip.extractall('RecibosDXC')

print('Extraido ok')
ZipFile.close()