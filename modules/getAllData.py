import requests



def DetallePed():
    peticion = requests.get("http://172.16.100.138:5508/")
    data = peticion.json()
    return data
def Gama():
    peticion = requests.get("http://172.16.100.138:5507/")
    data = peticion.json()
    return data
def Producto():
    peticion = requests.get("http://172.16.100.138:5506/")
    data = peticion.json()
    return data
def Pedido():
    peticion = requests.get("http://172.16.100.138:5505/")
    data = peticion.json()
    return data
def Oficina():
    peticion = requests.get("http://172.16.100.138:5504/")
    data = peticion.json()
    return data
def Cliente():
    peticion = requests.get("http://172.16.100.138:5503/")
    data = peticion.json()
    return data
def Empleado():
    peticion = requests.get("http://172.16.100.138:5502/")
    data = peticion.json()
    return data
def Pago():
    peticion = requests.get("http://172.16.100.138:5501/")
    data = peticion.json()
    return data