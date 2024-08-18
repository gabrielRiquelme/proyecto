import tarfile

file_tar = tarfile.open('primer.tar.gz', 'w:gz')
file_tar.add('doc.txt')
file_tar.close()