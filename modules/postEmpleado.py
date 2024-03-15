import json
import requests

def postEmpleado():
    newEmpleado = {
        "codigo_empleado": int(input("Ingrese codigo del empleado: ")),
        "nombre": input("Ingrese nombre del empleado: "),
        "apellido1": input("Ingrese apellido 1 del empleado: "),
        "apellido2": input("Ingrese apellido 2 del empleado: "),
        "extension": input("Ingresa la extension del empleado: "),
        "email": input("Ingrese email del empleado: "),
        "codigo_oficina": input("Ingrese el codigo de la oficina del empleado: "),
        "codigo_jefe": int(input("Ingrese codigo del jefe: ")),
        "puesto": input("Ingrese puesto del empleado: ")
    }

    peticion = requests.post("http://172.16.100.138:5502/", data=json.dumps(newEmpleado))
    res = peticion.json()
    res["Mensaje"] = "Empleado Guardado"
    return [res]