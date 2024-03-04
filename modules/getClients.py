import storage.cliente as cli

def getAllClienteName():
    clientName = []
    for i, val in enumerate(cli.cliente):
        clientName.append({
            "nombre_cliente": val.get("nombre_cliente"),
            "codigo_cliente": val.get("codigo_cliente")
            })
    return clientName

def getClienteCodigo(codigo):
    for val in cli.cliente:
        if(val.get("codigo_cliente") == codigo):
            return {
                "nombre_cliente": val.get("nombre_cliente"),
                "codigo_cliente": val.get("codigo_cliente")
            }

def getClienteCreditoCiudad(limiteCredito, ciudad):
    clientPremium = []
    for val in cli.cliente:
        if(val.get("limite_credito") >= limiteCredito and val.get("ciudad") == ciudad):
            clientPremium.append(val)
    return clientPremium

def getClienteRegion(region, ciudad):
    clientPremium = []
    for val in cli.cliente:
        if(
            val.get("region") == region and
            val.get("ciudad") == ciudad
        ):
            clientPremium.append(val)
    return