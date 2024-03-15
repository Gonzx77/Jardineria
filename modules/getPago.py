from datetime import datetime
from tabulate import tabulate
import modules.getAllData as data



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
                
    result.sort(key=lambda x: x[1], reverse=True)
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
    
    print(f"""
        1. Obtener todos los pagos realizados en 2008
        2. Obtener todos los pagos hechos con PayPal en 2008
        3. Obtener todas las posibles formas de pago
        4. Obtener todas las compras de un cliente
        0. Salir
        """)
    
    op = input("Ingrese opcion: ")
    while True:
        
        if op == "1":
            print("\n" + tabulate(getPagos2008(), headers=["Codigo cliente"], tablefmt="github"))
            break
        elif op == "2":
            print("\n" + tabulate(getPagoPaypal2008(), headers=["Codigo cliente", "ID", "Total"], tablefmt="github"))
            break
        elif op == "3":
            print("\n" + tabulate(getFormasPago(), headers=["Formas de pago"], tablefmt="github"))
            break
        
        elif op == "4":
            x = input("Ingrese codigo del cliente: ")
            if x in listCliente:
                print("\n" + tabulate(getComprasCliente(x), headers=["Codigo cliente", "Forma de pago", "ID Transaccion", "Fecha", "Total"], tablefmt="github"))
                break
            else:
                print(f"""Error: Este cliente no existe, los clientes existentes son:
                    {listCliente}""")
            
        elif op == "0":
            break
        
        else:
            print("Esta opcion no existe")
            op = input("Ingrese opcion: ")
            
            
    again = input(f""" \n Desea realizar otra consulta? (Si / No): """)
        
    if again.lower() != "si":
        print(f"""
            Gracias por usar nuestro sistema!
            """)
        exit()