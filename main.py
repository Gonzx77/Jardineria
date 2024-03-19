import os
import modules as modules

#json-server storage/pago.json -b 5506 & json-server storage/empleado.json -b 5503 & json-server storage/cliente.json -b 5501 & json-server storage/oficina.json -b 5505 & json-server storage/pedido.json -b 5507 & json-server storage/producto.json -b 5508 & json-server storage/gama_producto.json -b 5504 & json-server storage/detalle_pedido.json -b 5502


import modules.getOficinas as Oficina
import modules.getEmpleados as Empleado
import modules.getClientes as Cliente
import modules.getPedido as Pedido
import modules.getPago as Pago
import modules.getProducto as Producto


def menuInicial():
    while True:
        os.system("clear")
        print(f"""
            
            ----------- Menu Principal -----------

                    1. Cliente
                    2. Empleado
                    3. Oficina
                    4. Pago
                    5. Pedido
                    6. Producto
                    
                    0. Salir
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
            elif op == "0":
                exit()
            else:
                print("Esta opcion no existe")
            

        
menuInicial()