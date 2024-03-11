import storage.cliente as cli
from tabulate import tabulate

def getClientePais(x):
    result = []
    for val in cli.cliente:
        if(val.get("pais") == x):
            result.append([
                val.get("codigo_cliente"),
                val.get("nombre_cliente"),
                val.get("nombre_contacto"),
                val.get("telefono"),
                val.get("ciudad"),
                val.get("region"),
                val.get("pais")
            ])
    return result

def getClienteSinRegion():
    result = []
    for val in cli.cliente:
        if(val.get("region") == None):
            result.append([
                val.get("codigo_cliente"),
                val.get("nombre_cliente"),
                val.get("nombre_contacto"),
                val.get("telefono"),
                val.get("ciudad")
            ])
    return result

def getClienteRegion(x):
    result = []
    for val in cli.cliente:
        if(val.get("region") == x):
            result.append([
                val.get("codigo_cliente"),
                val.get("nombre_cliente"),
                val.get("nombre_contacto"),
                val.get("telefono"),
                val.get("ciudad"),
                val.get("region"),
                val.get("pais")
            ])
    return result

def getClienteCiudad(x):
    result = []
    for val in cli.cliente:
        if(val.get("ciudad") == x):
            result.append([
                val.get("codigo_cliente"),
                val.get("nombre_cliente"),
                val.get("nombre_contacto"),
                val.get("telefono"),
                val.get("ciudad"),
                val.get("region"),
                val.get("pais")
            ])
    return result

def menu():
    listPais = []
    listRegion = []
    listCiudad = []
    for val in cli.cliente:
        if val.get("pais") not in listPais:
            listPais.append(val.get("pais"))
    for val in cli.cliente:
        if val.get("region") not in listRegion:
            listRegion.append(val.get("region"))
    for val in cli.cliente:
        if val.get("ciudad") not in listCiudad:
            listCiudad.append(val.get("ciudad"))
    
    print(f"""
        1. Obtener clientes de un pais
        2. Obtener clientes con region indefinida
        3. Obtener clientes de una region
        4. Obtener clientes de una ciudad
        """)
    
    op = input("Ingrese opcion: ")
    
    while True:
        if op == "1":
            x = input("Ingrese el pais en el que desea buscar: ")
            if x in listPais:
                print("\n" + tabulate(getClientePais(x), headers=["Codigo", "Nombre", "Contacto", "Telefono", "Ciudad", "Region", "Pais"], tablefmt="github"))
                break
            else:
                print(f"""Error: Este pais no existe, los paises existentes son:
                    {listPais}""")
                
        elif op == "2":
            print("\n" + tabulate(getClienteSinRegion(), headers=["Codigo", "Nombre", "Contacto", "Telefono", "Ciudad"], tablefmt="github"))
            break
            
        elif op == "3":
            x = input("Ingrese la region en la que desea buscar: ")
            if x in listRegion:
                print("\n" + tabulate(getClienteRegion(x), headers=["Codigo", "Nombre", "Contacto", "Telefono", "Ciudad", "Region", "Pais"], tablefmt="github"))
                break
            else:
                print(f"""Error: Esta region no existe, las regiones existentes son:
                    {listRegion}""")
                
        elif op == "4":
            x = input("Ingrese la ciudad en la que desea buscar: ")
            if x in listCiudad:
                print("\n" + tabulate(getClienteCiudad(x), headers=["Codigo", "Nombre", "Contacto", "Telefono", "Ciudad", "Region", "Pais"], tablefmt="github"))
                break
            else:
                print(f"""Error: Esta ciudad no existe, las ciudades existentes son:
                    {listCiudad}""")
            
        else:
            print("Esta opcion no existe")
            menu()
        
        
        
        
    again = input(f""" \n Desea realizar otra consulta? (Si / No): """)
    
    if again.lower() == "si":
        import modules.again as againM
        againM.again()
    else:
        print(f"""
              Gracias por usar nuestro sistema!
              """)