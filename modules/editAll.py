import requests
import modules.getAllData as data

def Pago(id):
    listID = []
    for val in data.Pago():
        listID.append(val.get("id"))
        
    if id in listID:
        peticion = requests.get(f"http://154.38.171.54:5006/pagos?id={id}")
        peticion = peticion.json()
        print(peticion)
        print("Pago eliminado")
    else:
        print("Error, este Pago no existe !")
        
Pago(28)