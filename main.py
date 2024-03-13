import modules as modules

import modules.getOficinas as Oficina
import modules.getEmpleados as Empleado
#import modules.getClientes as Cliente
import modules.getPedido as Pedido
import modules.getPago as Pago
import modules.getProducto as Producto


def menuInicial():
    while True:
        print(f"""
            
            --- Menu Principal ---
            
            1. Clientes
            2. Empleados
            3. Oficina
            4. Pago
            5. Pedido
            6. Producto
            """)
        
        while True:
            op = input("Ingrese opcion: ")
            if op == "1":
                #Cliente.menu()
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
            else:
                print("Esta opcion no existe")
            
        
        
menuInicial()