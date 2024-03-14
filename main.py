import os
import modules as modules



import modules.getOficinas as Oficina

import modules.postEmpleado as PostEmpleado
import modules.getEmpleados as Empleado

import modules.postCliente as PostCliente
import modules.getClientes as Cliente

import modules.getPedido as Pedido

import modules.getPago as Pago

import modules.getProducto as Producto


def menuInicial():
    while True:
        os.system("clear")
        print(f"""
            
            ----------- Menu Principal -----------
            
            --- Consultas ---

                    1. Cliente
                    2. Empleado
                    3. Oficina
                    4. Pago
                    5. Pedido
                    6. Producto
                    
            --- Añadir datos ---
                    
                    7. Añadir Cliente
                    8. Añadir Empleado
            """)
        
        while True:
            op = input("Ingrese opcion: ")
            if op == "1":
                Cliente.menu()
                break
            elif op == "2":
                Empleado.menu()
                break
            elif op == "3":
                Oficina.menu()
                break
            elif op == "4":
                Pago.menu()
                break
            elif op == "5":
                Pedido.menu()
                break
            elif op == "6":
                Producto.menu()
                break
            elif op == "7":
                PostCliente.postCliente()
                break
            elif op == "8":
                PostEmpleado.postEmpleado()
                break
            else:
                print("Esta opcion no existe")
            

        
        
menuInicial()