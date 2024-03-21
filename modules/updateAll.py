import requests

# P A G O
def Pago(id):
    response = requests.get(f"http://154.38.171.54:5006/pagos/{id}")
    if response.status_code == 200:
        pago = response.json()
        print("Cliente actual:")
        print(pago)

        print("\nIngrese los nuevos valores (deje en blanco para mantener los valores actuales):")
        nuevo_codigo_cliente = input("Nuevo código de cliente: ").strip()
        nueva_forma_pago = input("Nueva forma de pago: ").strip()
        nueva_id_transaccion = input("Nueva ID de transacción: ").strip()
        nueva_fecha_pago = input("Nueva fecha de pago (YYYY-MM-DD): ").strip()
        nuevo_total = input("Nuevo total: ").strip()

        if nuevo_codigo_cliente:
            pago["codigo_cliente"] = int(nuevo_codigo_cliente)
        if nueva_forma_pago:
            pago["forma_pago"] = nueva_forma_pago
        if nueva_id_transaccion:
            pago["id_transaccion"] = nueva_id_transaccion
        if nueva_fecha_pago:
            pago["fecha_pago"] = nueva_fecha_pago
        if nuevo_total:
            pago["total"] = int(nuevo_total)

        response = requests.put(f"http://154.38.171.54:5006/pagos/{id}", json=pago)
        if response.status_code == 200:
            print("Pago actualizado correctamente.")
        else:
            print("Hubo un error al intentar actualizar el Pago.")
    else:
        print("No se pudo obtener el Pago.")
        

# E M P L E A D O
def Empleado(id): 
    response = requests.get(f"http://154.38.171.54:5003/empleados/{id}")
    if response.status_code == 200:
        empleado = response.json() 
        print("Empleado actual:")
        print(empleado)
        print("\nIngrese los nuevos valores (deje en blanco para mantener los valores actuales):")
        nuevo_codigo = input("Nuevo codigo empleado: ").strip()
        nuevo_nombre = input("Nuevo nombre empleado: ").strip()
        nuevo_apellido1 = input("Nuevo primer apellido: ").strip()
        nuevo_apellido2 = input("Nuevo segundo apellido: ").strip()
        nueva_extension = input("Nueva extensión: ").strip()
        nuevo_email = input("Nuevo email: ").strip()
        nuevo_codigo_oficina = input("Nuevo código de oficina: ").strip()
        nuevo_codigo_jefe = input("Nuevo código de jefe: ").strip()
        nuevo_puesto = input("Nuevo puesto: ").strip()

        if nuevo_codigo:
            empleado["codigo_empleado"] = int(nuevo_codigo)
        if nuevo_nombre:
            empleado["nombre"] = nuevo_nombre
        if nuevo_apellido1:
            empleado["apellido1"] = nuevo_apellido1
        if nuevo_apellido2:
            empleado["apellido2"] = nuevo_apellido2
        if nueva_extension:
            empleado["extension"] = nueva_extension
        if nuevo_email:
            empleado["email"] = nuevo_email
        if nuevo_codigo_oficina:
            empleado["codigo_oficina"] = nuevo_codigo_oficina
        if nuevo_codigo_jefe:
            empleado["codigo_jefe"] = nuevo_codigo_jefe
        if nuevo_puesto:
            empleado["puesto"] = nuevo_puesto

        response = requests.put(f"http://154.38.171.54:5003/empleados/{id}", json=empleado)
        if response.status_code == 200:
            print("Empleado actualizado correctamente.")
        else:
            print("Hubo un error al intentar actualizar el Empleado.")
    else:
        print("No se pudo obtener el Empleado.")
        
        
# C L I E N T E
def Cliente(id):
    response = requests.get(f"http://154.38.171.54:5001/cliente/{id}")
    if response.status_code == 200:
        cliente = response.json()
        print("Cliente actual:")
        print(cliente)

        print("\nIngrese los nuevos valores (deje en blanco para mantener los valores actuales):")
        nuevo_codigo = input("Nuevo codigo cliente: ").strip()
        nuevo_nombre_cliente = input("Nuevo nombre de cliente: ").strip()
        nuevo_nombre_contacto = input("Nuevo nombre de contacto: ").strip()
        nuevo_apellido_contacto = input("Nuevo apellido de contacto: ").strip()
        nuevo_telefono = input("Nuevo teléfono: ").strip()
        nuevo_fax = input("Nuevo fax: ").strip()
        nueva_linea_direccion1 = input("Nueva línea de dirección 1: ").strip()
        nueva_linea_direccion2 = input("Nueva línea de dirección 2: ").strip()
        nueva_ciudad = input("Nueva ciudad: ").strip()
        nueva_region = input("Nueva región: ").strip()
        nuevo_pais = input("Nuevo país: ").strip()
        nuevo_codigo_postal = input("Nuevo código postal: ").strip()
        nuevo_codigo_empleado_rep_ventas = input("Nuevo código de empleado de representante de ventas: ").strip()
        nuevo_limite_credito = input("Nuevo límite de crédito: ").strip()

        if nuevo_codigo:
            cliente["codigo_cliente"] = int(nuevo_codigo)
        if nuevo_nombre_cliente:
            cliente["nombre_cliente"] = nuevo_nombre_cliente
        if nuevo_nombre_contacto:
            cliente["nombre_contacto"] = nuevo_nombre_contacto
        if nuevo_apellido_contacto:
            cliente["apellido_contacto"] = nuevo_apellido_contacto
        if nuevo_telefono:
            cliente["telefono"] = nuevo_telefono
        if nuevo_fax:
            cliente["fax"] = nuevo_fax
        if nueva_linea_direccion1:
            cliente["linea_direccion1"] = nueva_linea_direccion1
        if nueva_linea_direccion2:
            cliente["linea_direccion2"] = nueva_linea_direccion2
        if nueva_ciudad:
            cliente["ciudad"] = nueva_ciudad
        if nueva_region:
            cliente["region"] = nueva_region
        if nuevo_pais:
            cliente["pais"] = nuevo_pais
        if nuevo_codigo_postal:
            cliente["codigo_postal"] = nuevo_codigo_postal
        if nuevo_codigo_empleado_rep_ventas:
            cliente["codigo_empleado_rep_ventas"] = int(nuevo_codigo_empleado_rep_ventas)
        if nuevo_limite_credito:
            cliente["limite_credito"] = int(nuevo_limite_credito)

        response = requests.put(f"http://154.38.171.54:5001/cliente/{id}", json=cliente)
        if response.status_code == 200:
            print("Cliente actualizado correctamente.")
        else:
            print("Hubo un error al intentar actualizar el Cliente.")
    else:
        print("No se pudo obtener el Cliente.")
        
        
# O F I C I N A
def Oficina(id):
    response = requests.get(f"http://154.38.171.54:5005/oficinas/{id}")
    if response.status_code == 200:
        oficina = response.json()
        print(oficina)

        print("\nIngrese los nuevos valores (deje en blanco para mantener los valores actuales):")
        nuevo_codigo = input("Nuevo codigo (AAA-AAA): ").strip()
        nueva_ciudad = input("Nueva ciudad: ").strip()
        nuevo_pais = input("Nuevo país: ").strip()
        nueva_region = input("Nueva región: ").strip()
        nuevo_codigo_postal = input("Nuevo código postal: ").strip()
        nuevo_telefono = input("Nuevo teléfono: ").strip()
        nueva_linea_direccion1 = input("Nueva línea de dirección 1: ").strip()
        nueva_linea_direccion2 = input("Nueva línea de dirección 2: ").strip()

        if nuevo_codigo:
            oficina["codigo_oficina"] = nuevo_codigo
        if nueva_ciudad:
            oficina["ciudad"] = nueva_ciudad
        if nuevo_pais:
            oficina["pais"] = nuevo_pais
        if nueva_region:
            oficina["region"] = nueva_region
        if nuevo_codigo_postal:
            oficina["codigo_postal"] = nuevo_codigo_postal
        if nuevo_telefono:
            oficina["telefono"] = nuevo_telefono
        if nueva_linea_direccion1:
            oficina["linea_direccion1"] = nueva_linea_direccion1
        if nueva_linea_direccion2:
            oficina["linea_direccion2"] = nueva_linea_direccion2

        response = requests.put(f"http://154.38.171.54:5005/oficinas/{id}", json=oficina)
        if response.status_code == 200:
            print("Oficina actualizada correctamente.")
        else:
            print("Hubo un error al intentar actualizar la Oficina.")
    else:
        print("No se pudo obtener la Oficina.")
        
        
# P E D I D O
def Pedido(id):
    response = requests.get(f"http://154.38.171.54:5007/pedidos/{id}")
    if response.status_code == 200:
        pedido = response.json()
        print("Pedido actual:")
        print(pedido)

        print("\nIngrese los nuevos valores (deje en blanco para mantener los valores actuales):")
        nuevo_codigo = input("Nuevo codigo: ").strip()
        nueva_fecha_pedido = input("Nueva fecha de pedido (YYYY-MM-DD): ").strip()
        nueva_fecha_esperada = input("Nueva fecha esperada (YYYY-MM-DD): ").strip()
        nueva_fecha_entrega = input("Nueva fecha de entrega (YYYY-MM-DD): ").strip()
        nuevo_estado = input("Nuevo estado: ").strip()
        nuevo_comentario = input("Nuevo comentario: ").strip()
        nuevo_codigo_cliente = input("Nuevo código de cliente: ").strip()

        if nuevo_codigo:
            pedido["codigo_pedido"] = nuevo_codigo
        if nueva_fecha_pedido:
            pedido["fecha_pedido"] = nueva_fecha_pedido
        if nueva_fecha_esperada:
            pedido["fecha_esperada"] = nueva_fecha_esperada
        if nueva_fecha_entrega:
            pedido["fechaEntrega"] = nueva_fecha_entrega
        if nuevo_estado:
            pedido["estado"] = nuevo_estado
        if nuevo_comentario:
            pedido["comentario"] = nuevo_comentario
        if nuevo_codigo_cliente:
            pedido["codigo_cliente"] = int(nuevo_codigo_cliente)

        response = requests.put(f"http://154.38.171.54:5007/pedidos/{id}", json=pedido)
        if response.status_code == 200:
            print("Pedido actualizado correctamente.")
        else:
            print("Hubo un error al intentar actualizar el Pedido.")
    else:
        print("No se pudo obtener el Pedido.")
        
        
# P R O D U C T O
def Producto(id):
    response = requests.get(f"http://154.38.171.54:5008/productos/{id}")
    if response.status_code == 200:
        producto = response.json()
        print("Producto actual:")
        print(producto)

        print("\nIngrese los nuevos valores (deje en blanco para mantener los valores actuales):")
        nuevo_codigo = input("Nuevo codigo: ").strip()
        nuevo_nombre = input("Nuevo nombre: ").strip()
        nueva_gama = input("Nueva gama: ").strip()
        nuevas_dimensiones = input("Nuevas dimensiones: ").strip()
        nuevo_proveedor = input("Nuevo proveedor: ").strip()
        nueva_descripcion = input("Nueva descripción: ").strip()
        nueva_cantidad = input("Nueva cantidad en stock: ").strip()
        nuevo_precio_venta = input("Nuevo precio de venta: ").strip()
        nuevo_precio_proveedor = input("Nuevo precio de proveedor: ").strip()

        if nuevo_codigo:
            producto["codigo_producto"] = nuevo_codigo
        if nuevo_nombre:
            producto["nombre"] = nuevo_nombre
        if nueva_gama:
            producto["gama"] = nueva_gama
        if nuevas_dimensiones:
            producto["dimensiones"] = nuevas_dimensiones
        if nuevo_proveedor:
            producto["proveedor"] = nuevo_proveedor
        if nueva_descripcion:
            producto["descripcion"] = nueva_descripcion
        if nueva_cantidad:
            producto["cantidadEnStock"] = int(nueva_cantidad)
        if nuevo_precio_venta:
            producto["precio_venta"] = float(nuevo_precio_venta)
        if nuevo_precio_proveedor:
            producto["precio_proveedor"] = float(nuevo_precio_proveedor)

        response = requests.put(f"http://154.38.171.54:5008/productos/{id}", json=producto)
        if response.status_code == 200:
            print("Producto actualizado correctamente.")
        else:
            print("Hubo un error al intentar actualizar el Producto.")
    else:
        print("No se pudo obtener el Producto.")
        
        
# G A M A
def Gama(id):
    response = requests.get(f"http://154.38.171.54:5004/gama/{id}")
    if response.status_code == 200:
        gama = response.json()
        print("Gama actual:")
        print(gama)

        print("\nIngrese los nuevos valores (deje en blanco para mantener los valores actuales):")
        nueva_gama = input("Nuva gama: ").strip()
        nueva_descripcion_texto = input("Nueva descripción de texto: ").strip()
        nuevo_descripcion_html = input("Nueva descripción HTML: ").strip()
        nueva_imagen = input("Nueva imagen: ").strip()

        if nueva_gama:
            gama["gama"] = nueva_gama
        if nueva_descripcion_texto:
            gama["descripcion_texto"] = nueva_descripcion_texto
        if nuevo_descripcion_html:
            gama["descripcion_html"] = nuevo_descripcion_html
        if nueva_imagen:
            gama["imagen"] = nueva_imagen

        response = requests.put(f"http://154.38.171.54:5004/gama/{id}", json=gama)
        if response.status_code == 200:
            print("Gama actualizada correctamente.")
        else:
            print("Hubo un error al intentar actualizar la Gama.")
    else:
        print("No se pudo obtener la Gama.")
        
        
# D E T A L L E - P E D I D O
def DetallePed(id):
    response = requests.get(f"http://154.38.171.54:5002/detalle_pedido/{id}")
    if response.status_code == 200:
        pedido = response.json()
        print("Pedido actual:")
        print(pedido)

        print("\nIngrese los nuevos valores (deje en blanco para mantener los valores actuales):")
        nuevo_codigo_producto = input("Nuevo código de producto: ").strip()
        nueva_cantidad = input("Nueva cantidad: ").strip()
        nuevo_precio_unidad = input("Nuevo precio por unidad: ").strip()
        nuevo_numero_linea = input("Nuevo número de línea: ").strip()

        if nuevo_codigo_producto:
            pedido["codigo_producto"] = nuevo_codigo_producto
        if nueva_cantidad:
            pedido["cantidad"] = int(nueva_cantidad)
        if nuevo_precio_unidad:
            pedido["precio_unidad"] = float(nuevo_precio_unidad)
        if nuevo_numero_linea:
            pedido["numero_linea"] = int(nuevo_numero_linea)

        response = requests.put(f"http://154.38.171.54:5002/detalle_pedido/{id}", json=pedido)
        if response.status_code == 200:
            print("Detalle de Pedido actualizado correctamente.")
        else:
            print("Hubo un error al intentar actualizar el Detalle de Pedido.")
    else:
        print("No se pudo obtener el Detalle de Pedido.")