import json
import requests
import modules.getAllData as data


def Pago(id):
    listID = []
    for val in data.Pago():
        listID.append(val.get("id"))
        
    if id in listID:
        requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
        print("Pago eliminado")
    else:
        print("Error, este Pago no existe !")

def Empleado(id):
    listID = []
    for val in data.Empleado():
        listID.append(val.get("id"))
        
    if id in listID:
        requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
        print("Empleado eliminado")
    else:
        print("Error, este Empleado no existe !")