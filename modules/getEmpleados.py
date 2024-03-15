from tabulate import tabulate
import modules.postEmpleado as postEmp
import requests
import os


def getAllData():
    peticion = requests.get("http://172.16.100.138:5502/")
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
        if(val.get("codigo_jefe") == None):
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
    os.system("clear")
    listJefes = []
    listOficinas = []
    for val in getAllData():
        if val.get("codigo_jefe") not in listJefes:
            listJefes.append(val.get("codigo_jefe"))
    for val in getAllData():
        if val.get("codigo_oficina") not in listOficinas:
            listOficinas.append(val.get("codigo_oficina"))
    
    while True:
        os.system("clear")
        print(f"""
            --- Menu Empleado ---
            
            1. Consultar
            2. Editar Datos Empleado
            0. Salir
            """)
        
        opP = input("Ingrese opcion: ")


        if opP == "1":
            os.system("clear")
            print(f"""
                1. Obtener todos los empleados de un Jefe
                2. Obtener jefe
                3. Obtener empleados que no son representantes de ventas
                4. Obtener empleados de una misma oficiona
                0. Salir
                """)
            break
            
        elif opP == "2":
                os.system("clear")
                print(f"""
                1. Añadir Empleado
                0. Salir
                """)
                break
        elif opP == "0":
            break
        else:
            print("Esta opcion no existe: ")
            input("Presione cualquier tecla para continuar...")
    
    
    while True:
        op = input("Ingrese opcion: ")
        if opP == "1":
            if op == "1":
                while True:
                    x = str(input("Ingrese codigo del Jefe: "))
                    if x in str(listJefes):
                        os.system("clear")
                        print(tabulate(getEmpleadoJefe(x), headers=["Nombre", "Apellido 1", "Apellido 2", "Email", "Puesto", "Codigo Jefe"], tablefmt="github"))
                        input(f"""
        Presiona cualquier tecla para continuar...""")
                        os.system("clear")
                        break
                    else:
                        print(f"""Error: Este Jefe no existe, los Jefes existentes son:
                            {listJefes}""")
                break
                    
            elif op == "2":
                os.system("clear")
                print(tabulate(getJefe(), headers=["Nombre", "Apellido 1", "Apellido 2", "Email", "Puesto"], tablefmt="github"))
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
                
            elif op == "3":
                os.system("clear")
                print(tabulate(getEmpleadoNoRepresntanteVentas(), headers=["Nombre", "Apellido 1", "Apellido 2", "Email", "Puesto"], tablefmt="github"))
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
            
            elif op == "4":
                while True:
                    x = input("Ingresa codigo de la oficina: ")
                    if x in listOficinas:
                        os.system("clear")
                        print(tabulate(getEmpleadoOficina(x), headers=["Nombre", "Apellido 1", "Apellido 2", "Email", "Puesto", "Codigo Jefe", "Oficina"], tablefmt="github"))
                        input(f"""
        Presiona cualquier tecla para continuar...""")
                        os.system("clear")
                        break
                    else:
                        print(f"""Error: Esta oficina no existe, las oficinas existentes son:
                            {listOficinas}""")
                break
                    
            elif op == "0":
                break
            
            else:
                print("Esta opcion no existe")
                op = input("Ingrese opcion: ")
        
        elif opP == "2":
            op = input("Ingrese opcion: ")
            if op == "1":
                os.system("clear")
                print(postEmp.postEmpleado())
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


    again = input(f"""
            
    Desea realizar otra consulta? (Si / No): """)
    
    if again.lower() != "si":
        print(f"""
            Gracias por usar nuestro sistema!
            """)
        exit()