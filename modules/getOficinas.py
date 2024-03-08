import storage.oficina as of
from tabulate import tabulate

def getOficinaCiudad():
    result = []
    for val in of.oficina:
        if(val.get("codigo_oficina") != None):
            result.append([
                val.get("codigo_oficina"),
                val.get("ciudad")
            ])
    return result

def getCiudadTelefonoDEEspaña():
    result = []
    for val in of.oficina:
        if(val.get("pais") == "España"):
            result.append([
                val.get("ciudad"),
                val.get("telefono")
            ])
    return result

def menu():
    print(F"""
        1. Obtener listado de todas las oficinas y su cudad
        2. Obtener listado de oficinas con su telefono de España""")
    op = int(input("Ingrese opcion: "))
    if op == 1:
        print(tabulate(getOficinaCiudad(), headers=["Codigo Oficina", "Ciudad"], tablefmt="grid"))
    elif op == 2:
        print(tabulate(getCiudadTelefonoDEEspaña(), headers=["Ciudad", "Telefono"], tablefmt="grid"))