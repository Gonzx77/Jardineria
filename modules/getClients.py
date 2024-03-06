import storage.cliente as cli

def getClienteEspaña():
    result = []
    for val in cli.cliente:
        if(val.get("pais") == "Spain"):
            result.append([
                val.get("nombre_cliente")
            ])
    return result