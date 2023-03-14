"""
1. Crear una clase usuario 
2. atributos: nombre, edad, curp
3. validar que CURP sea exacatamente a 18 caracteres exactamente
4. definir un metodo que muestre los dato del usaruo (solo atributos definidos)
5. definir un metodo que valide la edad del usario sea mayor o igual a 18 años 

"""

class Usuario:
    def __init__(self, nombre, edad, curp):
        self.__nombre = nombre
        if self.validar_edad(edad) == None:
            return "Edad invalida"
        self.__edad = edad
        if self.validar_curp(curp) == None:
            return "CURP invalido"
        self.__curp = curp

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if self.validar_edad(edad):
            self.__edad = edad
        else:
            print("Edad invalida")

    def get_curp(self):
        return self.__curp

    def set_curp(self, curp):
        if self.validar_curp(curp):
            self.__curp = curp

    def validar_curp(self, curp):
        if len(curp) == 18:
           
            return curp

    def mostrar_datos(self):
        return f"Usuario: {self.__nombre}\nEdad: {self.__edad}\nCURP: {self.__curp}"

    def validar_edad(self, edad):
        if edad >= 18:
            return edad
        
if __name__ == "__main__":
    usuario_1 = Usuario("Aldo", 18, "LOQI920821HYNZXV05")
    print(usuario_1.mostrar_datos())
    #usuario_1.set_edad(29)
    #print(usuario_1.mostrar_datos())
    #print(usuario_1.__curp)
