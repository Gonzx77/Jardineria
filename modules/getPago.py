import storage.pago as pag
from datetime import datetime
from tabulate import tabulate

def getPagos2008():
    result = []
    for val in pag.pago:
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
    for val in pag.pago:
        fecha = val.get("fecha_pago")
        metodo = val.get("forma_pago")
        if fecha != None:
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            año = fecha.year
            if año == 2008 and metodo == "PayPal":
                result.append([
                    val.get("codigo_cliente"),
                    val.get("id_transaccion"),
                    val.get("total"),
                ])
                
    result.sort(key=lambda x: x[1], reverse=True)
    return result

def getFormasPago():
    result = []
    for val in pag.pago:
        if [val.get("forma_pago")] not in result:
            result.append([
                val.get("forma_pago")
            ])
    return result

def menu():
    print(f"""
        1. Obtener todos los pagos realizados en 2008
        2. Obtener todos los pagos hechos con PayPal en 2008
        3. Obtener todas las posibles formas de pago
        """)
    op = int(input("Ingrese opcion: "))
    if op == 1:
        print(tabulate(getPagos2008(), headers=["Codigo cliente"], tablefmt="grid"))
    elif op == 2:
        print(tabulate(getPagoPaypal2008(), headers=["Codigo cliente", "ID", "Total"], tablefmt="grid"))
    elif op == 3:
        print(tabulate(getFormasPago(), headers=["Formas de pago"], tablefmt="grid"))