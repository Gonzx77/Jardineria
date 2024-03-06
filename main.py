from tabulate import tabulate

import modules.getOficinas as Oficina
import modules.getEmpleados as Empleado

#Devuelve un listado con el codigo de oficina y la ciudad donde hay oficinas
print("  #1  ",Oficina.getOficinaCiudad())

#Devuelve un listado con la ciudad y el telefono de las oficinas de españa
print("  #2  ",Oficina.getCiudadTelefonoDEEspaña())

#Devuelve un listado con el nombre, apellidos, y email de los empleados cuyo jefe tiene codigo igual a 7
print("  #3  ",Empleado.getClienteJefe7(7))

#Devuelve el nombre del puesto, nombre, y apellidos y email del jefe de la empresa
print("  #4  ",Empleado.getJefe())