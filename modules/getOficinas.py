from tabulate import tabulate
import modules.postOficina as postOfi
import requests
import os

def getAllData():
    peticion = requests.get("http://172.16.100.138:5504/")
    data = peticion.json()
    return data

def getOficinaCiudad():
    result = []
    for val in getAllData():
        if(val.get("codigo_oficina") != None):
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
        if (val.get("linea_direccion1") != None and val.get("linea_direccion1") != "") and (val.get("linea_direccion2") == None or val.get("linea_direccion2") == ""):
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
    

    while True:
        os.system("clear")
        print(f"""
            --- Menu Oficina ---
                
            1. Consultar
            2. Editar Datos Oficina
            0. Salir
            """)
        


        opP = input("Ingrese opcion: ")

        if opP == "1":
            os.system("clear")
            print(F"""
                1. Obtener listado de todas las oficinas y su ciudad
                2. Obtener listado de oficinas con su telefono de España
                3. Obtener todas las oficinas de un pais
                4. Obtener listado de las oficinas que solo cuentan con la primera linea de direccion
                0. Salir
                """)
            break

        elif opP == "2":
            os.system("clear")
            print(F"""
                1. Añadir Oficina
                0. Salir
                """)
            break
        elif opP == "0":
            break
        else:
            print("Esta opcion no existe")
            input("Presione cualquier tecla para continuar...")
        
    while True:
        if opP == "1":
            op = input("Ingrese opcion: ")
            if op == "1":
                os.system("clear")
                print(tabulate(getOficinaCiudad(), headers=["Codigo Oficina", "Ciudad"], tablefmt="github"))
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
                
            elif op == "2":
                os.system("clear")
                print(tabulate(getOficinaTelefonoDEEspaña(), headers=["Codigo Oficina", "Ciudad", "Telefono"], tablefmt="github"))
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
                
            elif op == "3":
                while True:
                    x = input("Ingrese pais: ")
                    if x in listPais:
                        os.system("clear")
                        print(tabulate(getOficinaPais(x), headers=["Codigo Oficina", "Ciudad", "Pais", "Telefono"], tablefmt="github"))
                        input(f"""
        Presiona cualquier tecla para continuar...""")
                        os.system("clear")
                        break
                    else:
                        print(f"""Error: Este pais no existe, los paises existentes son:
                            {listPais}""")
                break
                        
            elif op == "4":
                os.system("clear")
                print(tabulate(getOficinaSin2Direccion(), headers=["Codigo Oficina", "Ciudad", "Pais", "Telefono", "Direccion 1", "Direccion 2"], tablefmt="github"))
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
                
            elif op == "0":
                break
                        
            else:
                print("Esta opcion no existe")
        elif opP == "2":
            op = input("Ingrese opcion: ")
            if op == "1":
                os.system("clear")
                print(postOfi.postOficina())
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
            elif op == "0":
                break
            else:
                print("Esta opcion no existe")
        elif opP == "0":
            break
            
            
    again = input(f"""\n Desea realizar otra consulta? (Si / No): """)
    
    if again.lower() == "si":
        None
    else:
        print(f"""
              Gracias por usar nuestro sistema!
              """)
        exit()