import storage.pedido as ped
from datetime import datetime
from tabulate import tabulate

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
    return result

def getPedidosCancelados2009():
    result = []
    for val in ped.pedido:
        estado = val.get("estado")
        fecha = "/".join(val.get("fecha_pedido").split("-")[::-1])
        fecha = datetime.strptime(fecha, "%d/%m/%Y")
        año = fecha.year
        
        if estado == "Rechazado" and año == 2009:
            if val.get("comentario") == None:
                result.append([
                    val.get("codigo_pedido"),
                    "Ninguno"
                ])
            else:
                result.append([
                    val.get("codigo_pedido"),
                    val.get("comentario")
                ])
    return result

def getPedidosEnero():
    result = []   
    for val in ped.pedido:
        fecha = val.get("fecha_entrega")
        estado = val.get("estado")
        if estado == "Entregado" and fecha != None:
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            mes = fecha.month
            if mes == 1:
                if val.get("comentario") != None:
                    result.append([
                        val.get("codigo_pedido"),
                        val.get("comentario")
                    ])
                else:
                    result.append([
                        val.get("codigo_pedido"),
                        "Ninguno"
                    ])
    return result

def menu():
    print(f"""
          1. Obtener todos los posibles estados de un pedido
          2. Obtener todos los pedidos que se entregaron tarde
          3. Obtener todos los pedidos que se entregaron 2 o mas dias tarde
          4. Obtener todos los pedidos cancelados en 2009
          5. Obtener todos los pedidos entregados enero
          """)
    op = int(input("Ingrese opcion: "))
    if op == 1:
        print(tabulate(getEstadosPedido(), headers=["Estados"], tablefmt="grid"))
    elif op == 2:
        print(tabulate(getPedidosTarde(), headers=["Codigo pedido", "Codigo cliente", "fecha esperada", "fecha entregada", "Dias de retrazo", "Comentario"], tablefmt="grid"))
    elif op == 3:
        print(tabulate(getPedidos2DiasTarde(), headers=["Codigo pedido", "Codigo cliente", "fecha esperada", "fecha entregada", "Dias antes", "Comentario"], tablefmt="grid"))
    elif op == 4:
        print(tabulate(getPedidosCancelados2009(), headers=["Codigo pedido", "Comentario"], tablefmt="grid"))
    elif op == 5:
        print(tabulate(getPedidosEnero(), headers=["Codigo pedido", "Comentario"], tablefmt="grid"))