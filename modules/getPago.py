import storage.pago as pag
from datetime import datetime

def getPagos2008():
    result = []
    for val in pag.pago:
        
        fecha = val.get("fecha_pago")
        fecha = "/".join(val.get("fecha_pago").split("-")[::-1])

        fecha = datetime.strptime(fecha, "%d/%m/%Y")
        año = fecha.year
        
        if año == 2008:
            if str(val.get("codigo_cliente")) not in result:
                result.append([
                val.get("codigo_cliente")
                ])
                
    return result