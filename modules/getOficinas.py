import storage.oficina as of

def getOficinaCiudad():
    result = []
    for val in of.oficina:
        if(val.get("codigo_oficina") != None):
            result.append({
                "codigoOficina": val.get("codigo_oficina"),
                "ciudad": val.get("ciudad")
            })
    return result

def getCiudadTelefonoDEEspaña():
    result = []
    for val in of.oficina:
        if(val.get("pais") == "España"):
            result.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono")
            })
    return result