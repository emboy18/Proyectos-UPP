class CuentaJoven:
    def __init__(self, titular, balance,bonificacion=0.15):
        self.titular = titular
        self.balance = balance
        self.bonificacion = bonificacion
    
       
   
    def retirar (self, cantidad):
        if self.validar_retiro(cantidad):
            self.balance -= cantidad
        else:
            print("No hay dinero suficiente, no se puede realizar la transaccion")   
        
        if self.titular.edad <=25:
            self.balance -= cantidad
             
        else:
            print("Solo los titulares menores de 25 pueden retirar dinero de esta cuenta ") 
    
    def validar_retiro(self,retiro):
        if retiro <=self.balance:
            return True
        
    def mostrar_datos (self):
        print("Titular:", self.titular.nombre)
        if self.titular.edad <=25: 
            print("Tipo de cuenta: Cuenta Joven")
        else:
            print("Necesita crear una cuenta regular")
        print("Balance total: $", self.balance + (self.balance * self.bonificacion))  
        print("Bonificacion del:",self.bonificacion *100 ,"%")
               
class titular:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
titular_1 = titular("Aldo",16)
cuenta_joven1 = CuentaJoven(titular_1, 100)


titular_2 =titular("Camerina", 20)
cuenta_joven2 = CuentaJoven(titular_2,150)

print(cuenta_joven1.mostrar_datos())
cuenta_joven1.retirar(20)

print(cuenta_joven2.mostrar_datos())
cuenta_joven2.retirar(0)



