import storage.oficina as of

def getOficinaCiudad():
    result = []
    for val in of.oficina:
        if(val.get("codigo_oficina") != None):
            result.append([
                val.get("codigo_oficina"),
                val.get("ciudad")
            ])
    return result

def getCiudadTelefonoDEEspaña():
    result = []
    for val in of.oficina:
        if(val.get("pais") == "España"):
            result.append([
                val.get("ciudad"),
                val.get("telefono")
            ])
    return result