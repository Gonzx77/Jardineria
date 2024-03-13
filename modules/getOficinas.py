from tabulate import tabulate
import requests

def getAllData():
    peticion = requests.get("http://172.16.104.45:5505/")
    data = peticion.json()
    return data

def getOficinaCiudad():
    result = []
    for val in getAllData():
        if(val.get("codigo_oficina") != 0):
            result.append([
                val.get("codigo_oficina"),
                val.get("ciudad")
            ])
    return result

def getOficinaTelefonoDEEspaña():
    result = []
    for val in getAllData():
        if(val.get("pais") == "España"):
            result.append([
                val.get("codigo_oficina"),
                val.get("ciudad"),
                val.get("telefono")
            ])
    return result

def getOficinaPais(x):
    result = []
    for val in getAllData():
        if(val.get("pais") == x):
            result.append([
                val.get("codigo_oficina"),
                val.get("ciudad"),
                val.get("pais"),
                val.get("telefono")
            ])
    return result

def getOficinaSin2Direccion():
    result = []
    for val in getAllData():
        if (val.get("linea_direccion1") != 0 and val.get("linea_direccion1") != "") and (val.get("linea_direccion2") == 0 or val.get("linea_direccion2") == ""):
            result.append([
                val.get("codigo_oficina"),
                val.get("ciudad"),
                val.get("pais"),
                val.get("telefono"),
                val.get("linea_direccion1"),
                val.get("linea_direccion2")
            ])
    return result

def menu():
    listPais = []
    for val in getAllData():
        if val.get("pais") not in listPais:
            listPais.append(val.get("pais"))
    
    print(F"""
        1. Obtener listado de todas las oficinas y su ciudad
        2. Obtener listado de oficinas con su telefono de España
        3. Obtener todas las oficinas de un pais
        4. Obtener listado de las oficinas que solo cuentan con la primera linea de direccion
        0. Salir
        """)
    
    op = input("Ingrese opcion: ")
    while True:
        if op == "1":
            print(tabulate(getOficinaCiudad(), headers=["Codigo Oficina", "Ciudad"], tablefmt="github"))
            break
        
        elif op == "2":
            print(tabulate(getOficinaTelefonoDEEspaña(), headers=["Codigo Oficina", "Ciudad", "Telefono"], tablefmt="github"))
            break
        
        elif op == "3":
            x = input("Ingrese pais: ")
            if x in listPais:
                print(tabulate(getOficinaPais(x), headers=["Codigo Oficina", "Ciudad", "Pais", "Telefono"], tablefmt="github"))
                break
            else:
                print(f"""Error: Este pais no existe, los paises existentes son:
                    {listPais}""")
                
        elif op == "4":
            print(tabulate(getOficinaSin2Direccion(), headers=["Codigo Oficina", "Ciudad", "Pais", "Telefono", "Direccion 1", "Direccion 2"], tablefmt="github"))
            break
        
        elif op == "0":
            break
                
        else:
            print("Esta opcion no existe")
            op = input("Ingrese opcion: ")
            
            
    again = input(f"""\n Desea realizar otra consulta? (Si / No): """)
    
    if again.lower() == "si":
        0
    else:
        print(f"""
              Gracias por usar nuestro sistema!
              """)
        exit()