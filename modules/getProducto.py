from tabulate import tabulate
import modules.getAllData as data
import modules.postAll as post
import os



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
    os.system("clear")
    listGamas = []
    for val in data.Producto():
        if val.get("gama") not in listGamas:
            listGamas.append(val.get("gama"))
            
    while True:
        print(f"""
            1. Consulta
            2. Editar Datos Producto
            
            0. Salir
            """)
        
        opP = input("Ingrese opcion: ")
        
        if opP == "1":
            os.system("clear")
            print(f"""
                1. Obtener productos por gama y cantidad minima de stock
                
                0. Salir
                """)
            break
        
        elif opP == "2":
            os.system("clear")
            print(f"""
                1. Añadir Producto
                
                0. Salir
                """)
            break
        
        elif opP == "0":
            break
    
    while True:
        if opP == "1":
            op = input("Ingrese opcion: ")
            if op == "1":
                os.system("clear")
                while True:
                    gama = input("Ingrese gama que desea filtrar: ")
                    if gama in listGamas:
                        print(f"""Gama seleccionada: {gama}""")
                        stock = int(input("Ingrese cantidad minima en stock que desee filtrar: "))
                        print(tabulate(getProductOrnamentales(gama, stock), headers=["Gama", "ID producto", "Cantidad en stock", "Precio"], tablefmt="grid"))
                        input(f"""
    Presiona cualquier tecla para continuar...""")
                        os.system("clear")
                        break
                    else:
                        print(f"""Error: Esta gama no existe, las gamas existentes son:
                            {listGamas}""")
                break
            elif op == "0":
                break
            else:
                print("Esta opcion no existe")
                op = input("Ingrese opcion")
                
        elif opP == "2":
            op = input("Ingrese opcion: ")
            if op == "1":
                os.system("clear")
                print(post.Producto())
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
            
            elif op == "0":
                break
                
                
        
        elif opP == "0":
            break
        
        else:
            print("Esta opcion no existe")
            
    again = input(f""" \n Desea realizar otra consulta? (Si / No): """)
        
    if again.lower() != "si":
        print(f"""
            Gracias por usar nuestro sistema!
            """)
        exit()