class Email:
    def __init__(self,idCuenta,dominio,TipoDominio,contrasena):
        self.__idCuenta=idCuenta
        self.__dominio=dominio
        self.__TipoDominio=TipoDominio
        self.__contrasena=contrasena
        
    def retornaEmail(self):
       return self.__idCuenta + "@" + self.__dominio + "." + self.__TipoDominio
        
    def getDominio(self):
        return self.__dominio
   
    def CrearCuenta(self,direccion):
        partes=direccion.split("@")
        self.__idCuenta=partes[0]
        partes=partes[1].split(".")
        self.__dominio=partes[0]
        self.__TipoDominio=partes[1]
        self.__contrasena=input("ingrese la contraseña de la cuenta ")