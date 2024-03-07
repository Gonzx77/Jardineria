import storage.pedido as ped
from datetime import datetime, date

def getEstadosPedido():
    result = []
    for val in ped.pedido:
        if [val.get("estado")] in result:
            result
        else:
            result.append([val.get("estado")])
    return result

def getPedidosTarde():
    result = []
    for val in ped.pedido:
        if val.get("fecha_entrega") != None:
            fechaI = "/".join(val.get("fecha_esperada").split("-")[::-1])
            fechaF = "/".join(val.get("fecha_entrega").split("-")[::-1])
            
            start = datetime.strptime(fechaI, "%d/%m/%Y")
            end = datetime.strptime(fechaF, "%d/%m/%Y")
            
            dif = start.date() - end.date()
            dif = dif.days
            
            if dif < 0:
                if val.get("comentario") != None:
                    result.append([
                        val.get("codigo_pedido"),
                        val.get("codigo_cliente"),
                        val.get("fecha_esperada"),
                        val.get("fecha_entrega"),
                        dif,
                        val.get("comentario")
                        ])
                else:
                        result.append([
                        val.get("codigo_pedido"),
                        val.get("codigo_cliente"),
                        val.get("fecha_esperada"),
                        val.get("fecha_entrega"),
                        dif,
                        "No hay comentario"
                        ])
            else:
                result
        else:
            result
    return result

def getPedidos2DiasTarde():
    result = []
    for val in ped.pedido:
        if val.get("fecha_entrega") != None:
            fechaI = "/".join(val.get("fecha_esperada").split("-")[::-1])
            fechaF = "/".join(val.get("fecha_entrega").split("-")[::-1])
            
            start = datetime.strptime(fechaI, "%d/%m/%Y")
            end = datetime.strptime(fechaF, "%d/%m/%Y")
            
            dif = start.date() - end.date()
            dif = dif.days
            
            if dif >= 2:
                if val.get("comentario") != None:
                    result.append([
                        val.get("codigo_pedido"),
                        val.get("codigo_cliente"),
                        val.get("fecha_esperada"),
                        val.get("fecha_entrega"),
                        dif,
                        val.get("comentario")
                        ])
                else:
                        result.append([
                        val.get("codigo_pedido"),
                        val.get("codigo_cliente"),
                        val.get("fecha_esperada"),
                        val.get("fecha_entrega"),
                        dif,
                        "No hay comentario"
                        ])
            else:
                result
        else:
            result
    return result