from tabulate import tabulate
import requests


def getAllData():
    peticion = requests.get("http://172.16.104.45:5504/")
    data = peticion.json()
    return data

def getEmpleadoJefe(x):
    result = []
    for val in getAllData():
        if str(val.get("codigo_jefe")) == x:
            result.append([
                val.get("nombre"),
                val.get("apellido1"),
                val.get("apellido2"),
                val.get("email"),
                val.get("puesto"),
                val.get("codigo_jefe")
            ])
    return result

def getJefe():
    result = []
    for val in getAllData():
        if(val.get("codigo_jefe") == 0):
            result.append([
                val.get("puesto"),
                val.get("nombre"),
                val.get("apellido1"),
                val.get("apellido2"),
                val.get("email"),
                val.get("puesto")
            ])
    return result

def getEmpleadoNoRepresntanteVentas():
    result = []
    for val in getAllData():
        if(val.get("puesto") != "Representante Ventas"):
            result.append([
                val.get("nombre"),
                val.get("apellido1"),
                val.get("apellido2"),
                val.get("email"),
                val.get("puesto")
            ])
    return result

def getEmpleadoOficina(x):
    result = []
    for val in getAllData():
        if(val.get("codigo_oficina") == x):
            result.append([
                val.get("nombre"),
                val.get("apellido1"),
                val.get("apellido2"),
                val.get("email"),
                val.get("puesto"),
                val.get("codigo_jefe"),
                val.get("codigo_oficina")
            ])
    return result

def menu():
    listJefes = []
    listOficinas = []
    for val in getAllData():
        if val.get("codigo_jefe") not in listJefes:
            listJefes.append(val.get("codigo_jefe"))
    for val in getAllData():
        if val.get("codigo_oficina") not in listOficinas:
            listOficinas.append(val.get("codigo_oficina"))
    
    print(f"""
        1. Obtener todos los empleados de un Jefe
        2. Obtener jefe
        3. Obtener empleados que no son representantes de ventas
        4. Obtener empleados de una misma oficiona
        0. Salir
        """)
    
    op = input("Ingrese opcion: ")
    
    while True:
        if op == "1":
            x = str(input("Ingrese codigo del Jefe: "))
            if x in str(listJefes):
                print(tabulate(getEmpleadoJefe(x), headers=["Nombre", "Apellido 1", "Apellido 2", "Email", "Puesto", "Codigo Jefe"], tablefmt="github"))
                break
            else:
                print(f"""Error: Este Jefe no existe, los Jefes existentes son:
                    {listJefes}""")
                
        elif op == "2":
            print(tabulate(getJefe(), headers=["Nombre", "Apellido 1", "Apellido 2", "Email", "Puesto"], tablefmt="github"))
            break
            
        elif op == "3":
            print(tabulate(getEmpleadoNoRepresntanteVentas(), headers=["Nombre", "Apellido 1", "Apellido 2", "Email", "Puesto"], tablefmt="github"))
            break
        
        elif op == "4":
            x = input("Ingresa codigo de la oficina: ")
            if x in listOficinas:
                print(tabulate(getEmpleadoOficina(x), headers=["Nombre", "Apellido 1", "Apellido 2", "Email", "Puesto", "Codigo Jefe", "Oficina"], tablefmt="github"))
                break
            else:
                print(f"""Error: Esta oficina no existe, las oficinas existentes son:
                    {listOficinas}""")
                
        elif op == "0":
            break
        
        else:
            print("Esta opcion no existe")
            op = input("Ingrese opcion: ")
                
                
    again = input(f"""
            
    Desea realizar otra consulta? (Si / No): """)
    
    if again.lower() == "si":
        0
    else:
        print(f"""
            Gracias por usar nuestro sistema!
            """)
        exit()