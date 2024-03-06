import storage.pedido as ped

def getEstadosPedido():
    result = []
    for val in ped.pedido:
        if [val.get("estado")] in result:
            result
        else:
            result.append([val.get("estado")])
    return result