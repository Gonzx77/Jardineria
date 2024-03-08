import storage.cliente as cli
from tabulate import tabulate

def getClienteEspaña():
    result = []
    for val in cli.cliente:
        if(val.get("pais") == "Spain"):
            result.append([
                val.get("nombre_cliente")
            ])
    return result

def menu():
    print(f"""
          1. Obtener clientes de españa""")
    
    op = int(input("Ingrese opcion: "))
    if op == 1:
        print(tabulate(getClienteEspaña(), headers=["Nombre"], tablefmt="grid"))