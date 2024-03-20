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

def Cliente(id):
    listID = []
    for val in data.Cliente():
        listID.append(val.get("id"))
        
    if id in listID:
        requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
        print("Cliente eliminado")
    else:
        print("Error, este Cliente no existe !")
        
def Oficina(id):
    listID = []
    for val in data.Oficina():
        listID.append(val.get("id"))
        
    if id in listID:
        requests.delete(f"http://154.38.171.54:5005/oficinas/{id}")
        print("Oficina eliminada")
    else:
        print("Error, esta Oficina no existe !")
        
def Pedido(id):
    listID = []
    for val in data.Pedido():
        listID.append(val.get("id"))
        
    if id in listID:
        requests.delete(f"http://154.38.171.54:5007/pedidos/{id}")
        print("Pedido eliminado")
    else:
        print("Error, este Pedido no existe !")
        
def Producto(id):
    listID = []
    for val in data.Producto():
        listID.append(val.get("id"))
        
    if id in listID:
        requests.delete(f"http://154.38.171.54:5008/productos/{id}")
        print("Producto eliminado")
    else:
        print("Error, este Producto no existe !")