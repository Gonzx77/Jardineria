import storage.pedido as ped

def getEstadosPedido():
    result = []
    for val in ped.pedido:
        if {"Estado":val.get("estado")} not in result:
            result.append({"Estado": val.get("estado")})
    return result