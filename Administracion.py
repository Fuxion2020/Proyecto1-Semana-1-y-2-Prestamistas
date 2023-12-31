from ClassPrestamo import *
from Cliente import *
import pickle
import datetime

class Administracion:
    #Listas que usará el programa para guardar clientes y préstamos 
    def __init__(self):
        #Aqui se guardan los clientes
        self.clientes = []
    
    def buscar_cliente(self, nombre, cedula):
        """Busca un cliente por su nombre y cédula."""
        for cliente in self.clientes:
            if cliente.nombre == nombre and cliente.cedula == cedula:
                return cliente
        return None

    def menucito(self,opciones):
        #Es para que se lea la lista "opciones" y las numerice, así en el input solo hay que poner el número de la selcción
        print("----------------------------")
        for opcion in range(len(opciones)):
                print(f"{opcion+1} / {opciones[opcion]}")
                print("----------------------------")
    
                  
                
    def menu(self):
        #Listas que usará el programa para las opciones del menu
        opciones = ["Registrar cliente", "Registrar préstamo", "Revisar corte", "Ver clientes registrados", "Salir"]
        final = 0
        while final == 0:
            
            print(f"""
                    HOLA! 
                BIENVENIDO A
               "Préstamos C.A"

                """)
            self.menucito(opciones)

            eleccion = input("Ingrese el número de la opción que desee: ")
            if eleccion == "1":
                self.registrar_cliente()
                self.pause()       
            elif eleccion == "2":
                self.registrar_prestamo()
                self.pause()  
            elif eleccion == "3":
                self.revisar_corte()
                self.pause()      
            elif eleccion == "4":
                self.mostrar_clientes()
                self.pause()   
            elif eleccion == "5":
                final = final + 1
                print("Fin")
            else:
                print("Error, seleccione un número válido")
                self.pause()
            

    
    def registrar_cliente(self):
        #Si se desea añadir más de un cliente
        qty = (input("Cuántos clientes deseas agregar?: "))
        #Para no permitir letras ni símbolos
        while any(chr.isalpha() for chr in qty) or not qty.isdigit():
            qty = input("Error! Ingrese un numero: ")
        qty = int(qty)
        for i in range(qty):
            #Validacion de nombre
            nombre=input("- Ingrese el nombre del cliente: ")
            nombre=nombre.lower()
            nombre=nombre.title()
            #Para no permitir números ni símbolos
            while any(chr.isdigit() for chr in nombre) or not nombre.isalpha():
                nombre = input("Error! Ingrese el nombre del cliente: ")
                nombre=nombre.lower()
                nombre=nombre.title()
                
            #Validacion de DNI
            cedula =input("- Ingrese el DNI del cliente: ")
            #Validacion si el DNI tiene solo números
                    
            while any(chr.isalpha() for chr in cedula) or not cedula.isdigit():
                cedula = input("Error! Ingrese el DNI del cliente:  ")

            prestamos = []   
            nuevo_cliente = Cliente(nombre,cedula,prestamos)
            self.clientes.append(nuevo_cliente)
            print(f">> Se ha registrado un nuevo cliente: {nombre} ")



    def pause(self):
        #Pausa activa que se usan en casi todos los metodos, así la pantalla se ve más organizada al hacerle run
        print("Toque cualquier botón para volver al menú")
        pause = input(" ")
        if pause == "":
         pass
        else:
         pass
    


    def registrar_prestamo(self):
        #Pide los datos del cliente y del préstamo
        #Validacion de DNI
        cedula =input("Ingrese el DNI del cliente: ")
        #Validacion si el DNI tiene solo números          
        while any(chr.isalpha() for chr in cedula) or not cedula.isdigit():
            cedula = input("Error! Ingrese el DNI del cliente:  ")
        existencia = 0
        if True:
            for dni in self.clientes:
                if dni.cedula == cedula:
                    nombre = dni.nombre
                    existencia = existencia + 1
        if existencia > 0:        
            #Validación del monto
            while True:
                try:
                    monto = input("Ingrese el monto del préstamo: ")
                    if monto == " ":
                        raise ValueError
                    if not monto.isdigit():
                        raise ValueError
                    monto = float(monto)
                    if monto <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Error! El monto tiene que ser un número mayor a 0 y no puede haber letras.")
                    
            fecha = datetime.date.today()
            #Busca al cliente en la lista de clientes
            cliente = self.buscar_cliente(nombre, cedula)
            #Si el cliente existe, le crea un nuevo préstamo y lo agrega a la lista de préstamos
            if cliente:
                prestamo = cliente.solicitar_prestamo(monto,fecha)
                print(f"<<<Se ha realizado el préstamo de {monto} a {nombre} con éxito.>>>>")
                print("Estado del prestamo:")
                print(prestamo.obtener_estado())
            #Si el cliente no existe, le avisa al usuario
            else:
                print(f"No se encontró al cliente con cédula {cedula}.")



 
    def revisar_corte(self):
        #Recorre la lista de clientes 
        for cliente in self.clientes:
            print(f"Cliente: {cliente.nombre}")
            print(f"Cédula: {cliente.cedula}")
            #Recorre la lista de préstamos de cada cliente 
            for prestamo in cliente.prestamos:
                fecha_vencimiento = prestamo.fecha_final
                #Pide a la compañía que ingrese la fecha que desea consultar
                fecha_consulta = input("Ingrese la fecha que desea consultar el corte (xx/bb/yyyy): ")
                # Crea una variable para controlar el bucle
                fecha_valida = False
                # Mientras la fecha no sea válida, se repite el bucle
                while not fecha_valida:
                    # Intenta convertir la fecha ingresada a un objeto datetime
                    try:
                        fecha_consulta = datetime.datetime.strptime(fecha_consulta, "%d/%m/%Y")
                        #Convierte el objeto datetime.datetime a un objeto datetime.date
                        fecha_consulta = fecha_consulta.date()
                        #Valida que la fecha ingresada esté dentro del rango de los 24 días desde la fecha del préstamo
                        if prestamo.fecha <= fecha_consulta <= fecha_vencimiento:
                            dias_transcurridos = (fecha_consulta - prestamo.fecha).days
                            monto_cobrado = prestamo.monto * (1 + prestamo.tasa_interes())
                            monto_diario = (monto_cobrado / 24)
                            total_cobrado = monto_diario * dias_transcurridos
                            total_pendiente = monto_cobrado - total_cobrado
    
                            print(f"- Total cobrado: {round((total_cobrado),2)}")
                            print(f"- Total pendiente: {round((total_pendiente),2)}")
                            print("<---------------------------->")
                            # Si la fecha es válida, cambia el valor de la variable a True para salir del bucle
                            fecha_valida = True
                        else:
                            #Si la fecha ingresada no está dentro del rango, muestra un mensaje de error y pide otra fecha
                            print("La fecha ingresada no es válida. Debe estar dentro de los 24 días desde la fecha del préstamo.")
                            fecha_consulta = input("Ingrese la fecha que desea consultar el corte (xx/bb/yyyy): ")
                    except ValueError:
                        #Si la fecha ingresada no tiene el formato correcto, muestra un mensaje de error y pide otra fecha
                        print("La fecha ingresada no tiene el formato correcto. Debe ser xx/bb/yyyy.")
                        fecha_consulta = input("Ingrese otra fecha que desea consultar el corte (xx/bb/yyyy): ")




    def mostrar_clientes(self):
        with open("Archivolista", "wb") as Lista_binaria:
            pickle.dump(self.clientes, Lista_binaria)

        with open("Archivolista", "rb") as Listaarchivada:
            Lista_binaria = pickle.load(Listaarchivada)
            # Aqui crea un diccionario vacío para guardar los clientes
            clientes_dict = {}
            # Aqui recorre la lista de clientes y los agrega al diccionario usando su nombre como clave
            for cliente in Lista_binaria:
                clientes_dict[cliente.nombre] = cliente
            # Aqui muestra el diccionario de clientes
            for nombre, cliente in clientes_dict.items():
                # Format para mostrar el nombre y la cédula del cliente
                print(" Cliente: {}     Cédula: {}".format(nombre, cliente.cedula))
                # Format para mostrar los datos de los préstamos del cliente
                for prestamo in cliente.prestamos:
                    print("Monto del préstamo: {:.2f}, Fecha: {}".format(prestamo.monto, prestamo.fecha ))
                print("<<<<<--------------->>>>>")


    

