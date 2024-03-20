import json
import requests


def Pago(id):
    peticion =  requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
    res = peticion.json()
    res["Mensaje"] = "Pago Eliminado"
    return [res]