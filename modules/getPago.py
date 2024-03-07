import storage.pago as pag
from datetime import datetime

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