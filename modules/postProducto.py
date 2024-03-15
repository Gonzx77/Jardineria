import json
import requests

def postProducto():
    newProducto = {
        "codigo_pedido": int(input("Ingrese codigo del pedido: ")),
        "fecha_pedido": input("Ingrese fecha del pedido: "),
        "fecha_esperada": input("Ingrese la fecha del pedido: "),
        "fecha_entrega": input("Ingrese fecha de entrega del pedido: "),
        "estado": input("Ingrese estado del pedido: "),
        "comentario": input("Ingrese comentario del pedido: "),
        "codigo_cliente": int(input("Ingrese codigo del cliente: "))
    }

    peticion = requests.post("http://192.168.1.43:5506/", data=json.dumps(newProducto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]