import csv
from clases1 import Email

def CuentaArchi(archivo):
    validas=[]
    with open("archi1poo.txt","r")as archivo:
        for linea in archivo:
            direccion=linea.strip()
            if '@' in direccion and '.' in direccion:
                cuenta=Email("","","","")
                cuenta.CrearCuenta(direccion)
                validas.append(cuenta)
            else:
                print(f"la direccion {direccion} es invalida ")
    return validas 
