from clases1 import Email
import funciones1


if __name__=='__main__': 
    #Ejercicio 1
    nombre=input("ingrese su nombre ")
    direccion=input("ingrese su direccion de correo electronico ")
    cuenta=Email("","","","")
    cuenta.CrearCuenta(direccion)
    print (f"El correo electroico {nombre} corresponde a la cuenta {cuenta.retornaEmail()} . ")
    #Ejercicio 2
    cuenta.ModContra()
    #Ejercicio 3
    direc=input("ingrese su direccion de correo para crear un objeto")
    email=Email("","","","")
    email.CrearCuenta(direc)
    print(f"el correo creado a partir de la direccion es {email.retornaEmail()}")
    #Ejercicio 4
    archivo="archi1poo.txt" 
    cuentas_validas=CuentaArchi(archivo)
    print(f"el numero de cuentas validas es de {len(cuentas_validas)} y las cuentas validas son: \n")
    for cuenta in cuentas_validas:
        print(cuenta.retornaEmail())
        
        
        
        
        