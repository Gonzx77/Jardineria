import json
import requests

def postOficina():
    newOficina = {
        "codigo_oficina": input("Ingrese codigo de la oficina: "),
        "ciudad": input("Ingrese ciudad de la oficina: "),
        "pais": input("Ingrese pais de la oficina: "),
        "region": input("Ingrese region de la oficina: "),
        "codigo_postal": input("Ingrese codigo postal de la oficina: "),
        "telefono": input("Ingrese telefono de la oficina: "),
        "linea_direccion1": input("Ingrese direccion 1 de la oficna: "),
        "linea_direccion2": input("Ingrese direccion 2 de la oficina: ")
    }

    peticion = requests.post("http://192.168.1.43:5504/", data=json.dumps(newOficina))
    res = peticion.json()
    res["Mensaje"] = "Oficina Guardada"
    return [res]