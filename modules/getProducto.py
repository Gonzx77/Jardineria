from tabulate import tabulate
import modules.getAllData as data



def getProductOrnamentales(gama, stock):
    result = []
    for val in data.Producto():
        if val.get("gama") == gama and val.get("cantidad_en_stock") > stock:
            result.append([
                val.get("gama"),
                val.get("codigo_producto"),
                val.get("cantidad_en_stock"),
                val.get("precio_venta")
            ])
            
    return result

def menu():
    listGamas = []
    for val in data.Producto():
        if val.get("gama") not in listGamas:
            listGamas.append(val.get("gama"))
            
    print(f"""
        1. Obtener productos por gama y cantidad minima de stock
        0. Salir
        """)
    
    op = input("Ingrese opcion: ")
    while True:
        if op == "1":
            gama = input("Ingrese gama que desea filtrar: ")
            while True:
                if gama in listGamas:
                    print(f"""Gama seleccionada: {gama}""")
                    stock = int(input("Ingrese cantidad minima en stock que desee filtrar: "))
                    print(tabulate(getProductOrnamentales(gama, stock), headers=["ID producto", "Cantidad en stock", "Precio"], tablefmt="grid"))
                    break
                else:
                    print(f"""Error: Esta gama no existe, las gamas existentes son:
                        {listGamas}""")
                    gama = input("Ingrese gama que desea filtrar: ")
            break
        elif op == "0":
            break
        else:
            print("Esta opcion no existe")
            op = input("Ingrese opcion")
            
    again = input(f""" \n Desea realizar otra consulta? (Si / No): """)
        
    if again.lower() != "si":
        print(f"""
            Gracias por usar nuestro sistema!
            """)
        exit()