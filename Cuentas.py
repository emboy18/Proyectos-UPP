"""
1. Crear clase cuentas 
2. Para poder crear una cuenta es necesario pasarle su respectivo usuario 
3. El deposito inicial de apertura es opcional 
4. Crear metodos retirar() y deposito() de los atributos que solo seran modificables atraves de los setters
5. crear un metodo mostrar_datos() que muestre nombre de usuario y balance total.
"""

from Usuario import Usuario


class Cuenta:
    def __init__(self, usuario: Usuario, balance=0):
        self.__usuario = usuario
        self.__balance = balance

    def retirar(self, retiro):
        if self.validar_retiro(retiro):
            self.__balance -= retiro
        else:
            print("No hay dinero suficiente, no se puede realizar la transaccion")
    
    def deposito (self, balance):
        if balance >0:
            self.__balance = self.__balance + balance
        
        

    def validar_retiro(self, retiro):
        # Validar suficiente saldo
        if retiro <= self.__balance:
            return True

    def mostrar_balance(self):
        return f"Balance total: {self.__balance}"
        

if __name__ == "__main__":
    usuario_1 = Usuario ( "Aldo",18, "LOQI920821HYNZXV05")
    cuenta_1 = Cuenta(usuario_1,10) 
    cuenta_1.retirar(15)
    cuenta_1.deposito(0)
    
    print(usuario_1.mostrar_datos())
    print(cuenta_1.mostrar_balance())
    
    