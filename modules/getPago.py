from datetime import datetime
from tabulate import tabulate
import modules.getAllData as data
import modules.postAll as post
import os


def getPagos2008():
    result = []
    for val in data.Pago():
        fecha = val.get("fecha_pago")

        fecha = datetime.strptime(fecha, "%Y-%m-%d")
        año = fecha.year
        
        if año == 2008:
            if str(val.get("codigo_cliente")) not in result:
                result.append([
                val.get("codigo_cliente")
                ])
                
    return result

def getPagoPaypal2008():
    result=[]
    for val in data.Pago():
        fecha = val.get("fecha_pago")
        metodo = val.get("forma_pago")
        if fecha != None:
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            año = fecha.year
            if año == 2008 and metodo == "PayPal":
                result.append([
                    val.get("codigo_cliente"),
                    val.get("id_transaccion"),
                    val.get("total")
                ])
                
    result.sort(key=lambda x: x[2], reverse=True)
    return result

def getFormasPago():
    result = []
    for val in data.Pago():
        if [val.get("forma_pago")] not in result:
            result.append([val.get("forma_pago")])
    return result

def getComprasCliente(a):
    result = []
    for val in data.Pago():
        if str(val.get("codigo_cliente")) == a:
            result.append([
                val.get("codigo_cliente"),
                val.get("forma_pago"),
                val.get("id_transaccion"),
                val.get("fecha_pago"),
                val.get("total")
            ])
            
    return result


def menu():
    listCliente = []
    for val in data.Pago():
        if str(val.get("codigo_cliente")) not in listCliente:
            listCliente.append(str(val.get("codigo_cliente")))
            
    while True:        
    
        os.system("clear")
        print(f"""
                --- Menu Pago ---
                
                1. Consultar
                2. Editar Datos pago
                
                0. Salir
                """)
        
        opP = input("Ingrese opcion: ")
        
        if opP == "1":
            os.system("clear")
            print(f"""
                1. Obtener todos los pagos realizados en 2008
                2. Obtener todos los pagos hechos con PayPal en 2008
                3. Obtener todas las posibles formas de pago
                4. Obtener todas las compras de un cliente
                
                0. Salir
                """)
            break
        
        elif opP == "2":
            os.system("clear")
            print(f"""
                1. Añadir Cliente
                
                0. Salir
                """)
            break
        
        elif opP == "0":
            break
        
        else:
            print("Esta opcion no existe")
            input("Presione cualquier tecla para continuar...")
        
    
    while True:
        if opP == "1":
            op = input("Ingrese opcion: ")
            if op == "1":
                os.system("clear")
                print("\n" + tabulate(getPagos2008(), headers=["Codigo cliente"], tablefmt="github"))
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
            elif op == "2":
                os.system("clear")
                print("\n" + tabulate(getPagoPaypal2008(), headers=["Codigo cliente", "ID", "Total"], tablefmt="github"))
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
            elif op == "3":
                os.system("clear")
                print("\n" + tabulate(getFormasPago(), headers=["Formas de pago"], tablefmt="github"))
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
            
            elif op == "4":
                while True:
                    x = input("Ingrese codigo del cliente: ")
                    if x in listCliente:
                        os.system("clear")
                        print("\n" + tabulate(getComprasCliente(x), headers=["Codigo cliente", "Forma de pago", "ID Transaccion", "Fecha", "Total"], tablefmt="github"))
                        input(f"""
    Presiona cualquier tecla para continuar...""")
                        os.system("clear")
                        break
                    else:
                        print(f"""Error: Este cliente no existe, los clientes existentes son:
                            {listCliente}""")
                break
                
            elif op == "0":
                break
            
            else:
                print("Esta opcion no existe")
                
        elif opP == "2":
            op = input("Ingrese opcion: ")
            if op == "1":
                os.system("clear")
                print(post.Pago())
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
            elif op == "0":
                break
            else:
                print("Esta opcion no existe")
                
        elif opP == "0":
            break

                
            
            
    again = input(f""" \n Desea realizar otra consulta? (Si / No): """)
        
    if again.lower() != "si":
        print(f"""
            Gracias por usar nuestro sistema!
            """)
        exit()