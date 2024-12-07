#Defina una clase base MenuItem: esta clase
#  debe tener atributos como nombre, precio y un método para calcular el precio total

#Cree subclases para diferentes tipos de elementos de menú: herede de MenuItem y 
# defina propiedades específicas para cada tipo (por ejemplo, bebida, aperitivo, plato principal).


# Defina una clase de pedido: esta clase debe tener una lista de objetos y métodos MenuItem para 
# agregar artículos, calcular el monto total de la factura y, potencialmente, aplicar descuentos 
# específicos según la composición del pedido.
class MenuItem():
    def __init__(self, nombre :str, precio : float):  # clase principal, nombre y precio
        self.nombre = nombre                           
        self.precio = precio        


    def neto(self):                                  # funcion donde queda guardado el precio   
        return self.precio


class  Almuerzo(MenuItem):
    def __init__(self, nombre : str, precio : float, sopa: bool): # mismos datos que el padre con la diferencia 
        super().__init__(nombre, precio)                          # de que este se le tiene sopa o no, haciendo
        if sopa == True:                                          # "descuento"si pide sin sopa
            self.sopa = "con sopa"
        else:
            self.sopa = "sin sopa"
            self.precio = self.precio -500

  #  def mostrar(self):
  #      return f"El cliente pidio {self.nombre,self.sopa}, eso cuesta: \n{self.precio} "
    

class Jugo(MenuItem):                                            
    def __init__(self, nombre: str, precio: float, agua:bool):   # mismos datos que el padre con la diferencia 
        super().__init__(nombre, precio)                         # de que si el jugo es con agua o en leche, 
        if agua == True:                                         # afectando en el precio
            self.agua = "Jugo en agua"
        else:
            self.agua = "Jugo en leche"
            self.precio = self.precio +1500
    
    
#    def mostrar(self):
#        return f"El cliente pidio {self.nombre,self.agua}, eso cuesta: \n{self.precio} "
    
        
class Postre(MenuItem):
    def __init__(self, nombre:str, precio: float, extra: bool):   # Mismos datos que en el padre con la diferencia
        super().__init__(nombre, precio)                           # de que tiene el dato de pedir mas grande o normal, 
        if extra == False:                                        # Alterando en el precio al final
            self.extra= "Postre normal"
        else:
            self.extra = "Postre Grande"
            self.precio = self.precio +2000


  #  def mostrar(self):
  #      return f"El cliente pidio {self.nombre,self.grande}, eso cuesta: \n{self.precio} "
        

class Order:
    def __init__(self):                          #lista donde quedara toda la cuenta
        self.lista_cuenta = []
          
    def añadidura(self, item: "MenuItem"):
        self.lista_cuenta.append(item)
    
    def cuenta(self):
        self.total = float(0)                     # suma de producto por producto hasta tener un total neto
        
        for item in self.lista_cuenta:
            self.total += item.neto()

        return self.total

    
#    def mostrar(self):
 #       return f"{self.lista_cuenta},con un total de { self.total}"   

#probamos el codigo
cliente = Order()                                             
cliente.añadidura(Jugo("maracuya", 5000, False))   
cliente.añadidura(Almuerzo("corriente", 12000, False))
cliente.añadidura(Postre("wafles", 2500, True))
cliente.añadidura(Jugo("fresa", 5000, True))   
cliente.añadidura(Almuerzo("pescado", 20000, False))
cliente.añadidura(Postre("fresas con crema", 3000, True))
cliente.añadidura(Jugo("mora", 5000, False))   
cliente.añadidura(Almuerzo("bandeja paisa", 25000, True))
cliente.añadidura(Postre("arequipe", 1000, True))
cliente.añadidura(Jugo("mango", 5000, True))   
cliente.añadidura(Almuerzo("corriente", 25000, True))
cliente.añadidura(Postre("brownie", 1000, True))

print(f"Total a pagar: ${cliente.cuenta()} pesos ")

#si no estoy mal 119.500 pesos
