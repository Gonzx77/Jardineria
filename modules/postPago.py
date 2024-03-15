import json
import requests

def postPago():
    newPago = {
        "codigo_cliente": int(input("Ingrese codigo del cliente: ")),
        "forma_pago": input("Ingrese forma de pago: "),
        "id_transaccion": input("Ingrese ID de transaccion: "),
        "fecha_pago": input("Ingrese fecha del pago: "),
        "total": int(input("Ingrese valor total del pago: "))
    }

    peticion = requests.post("http://192.168.1.43:5501/", data=json.dumps(newPago))
    res = peticion.json()
    res["Mensaje"] = "Pago Guardado"
    return [res]