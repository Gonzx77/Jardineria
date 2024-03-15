import json
import requests

def postCliente():
    newCliente = {
        "codigo_cliente": int(input("Ingrese codigo del cleinte: ")),
        "nombre_cliente": input("Ingrese nombre del cliente: "),
        "nombre_contacto": input("Ingrese nombre del contacto del cliente: "),
        "apellido_contacto": input("Ingrese apellido del contacto del cliente: "),
        "telefono": input("Ingrese el telefono del cliente: "),
        "fax": input("Ingresa el fax del cliente: "),
        "linea_direccion1": input("Ingresa direccion 1 del cliente: "),
        "linea_direccion2": input("Ingresa direccion 2 del cliente: "),
        "ciudad": input("Ingresa la ciudad del cliente: "),
        "region": input("Ingresa la region del cliente: "),
        "pais": input("Ingrese pais del cliente: "),
        "codigo_postal": input("Ingrese codigo postal del cliente: "),
        "codigo_empleado_rep_ventas": int(input("Ingrese codigo del representante de ventas: ")),
        "limite_credito": float(input("Ingrese limite de credito del cliente: "))
    }

    peticion = requests.post("http://192.168.1.43:5503/", data=json.dumps(newCliente))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]