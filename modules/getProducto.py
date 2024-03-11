import storage.producto as pro
from tabulate import tabulate

def getProductOrnamentales():
    result = []
    for val in pro.producto:
        if val.get("gama") == "Ornamentales" and val.get("cantidad_en_stock") > 100:
            result.append([
                val.get("gama"),
                val.get("codigo_producto"),
                val.get("cantidad_en_stock"),
                val.get("precio_venta")
            ])
            
    return result

def menu():
    print(f"""
        1. Obtener productos de la gama ornamentales
        0. Salir
        """)
    op = input("Ingrese opcion")
    while True:
        if op == "1":
            print(tabulate(getProductOrnamentales(), headers=["ID producto", "Cantidad en stock", "Precio"], tablefmt="grid"))
            break
        elif op == "0":
            break
        else:
            print("Esta opcion no existe")
            op = input("Ingrese opcion")