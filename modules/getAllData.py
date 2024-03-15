import requests



def DetallePed():
    peticion = requests.get("http://192.168.1.43:5508/")
    data = peticion.json()
    return data
def Gama():
    peticion = requests.get("http://192.168.1.43:5507/")
    data = peticion.json()
    return data
def Producto():
    peticion = requests.get("http://192.168.1.43:5506/")
    data = peticion.json()
    return data
def Pedido():
    peticion = requests.get("http://192.168.1.43:5505/")
    data = peticion.json()
    return data
def Oficina():
    peticion = requests.get("http://192.168.1.43:5504/")
    data = peticion.json()
    return data
def Cliente():
    peticion = requests.get("http://192.168.1.43:5503/")
    data = peticion.json()
    return data
def Empleado():
    peticion = requests.get("http://192.168.1.43:5502/")
    data = peticion.json()
    return data
def Pago():
    peticion = requests.get("http://192.168.1.43:5501/")
    data = peticion.json()
    return data