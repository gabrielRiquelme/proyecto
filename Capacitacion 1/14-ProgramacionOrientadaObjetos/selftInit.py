#class FabricaTelefonos():
 #   marca = "Samsung"
 #   
  #  def elaborarHuawei(self):
 #       self.marca = "Huawei"
#
#telefono = FabricaTelefonos()
#print(telefono.marca)

#telefono.elaborarHuawei()
#print(telefono.marca)
#

class FabricaTelefonos():
    def __init__(self, marca, color): #Constructor#
        self.marca = marca
        self.color = color

telefono = FabricaTelefonos('Xiaomi','Blanco')
print(telefono.marca)
print(telefono.color)