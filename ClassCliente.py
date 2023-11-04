import datetime
import pickle
from ClassPrestamo import *

class Cliente:
    def __init__(self, nombre, cedula, saldo):
        self.nombre = nombre
        self.cedula = cedula
        self.saldo = saldo
        self.prestamos = []     #Lista vacía para guardar los préstamos del cliente


    def solicitar_prestamo(self, monto, fecha):
        prestamo = Prestamo(monto, fecha, self)
        self.prestamos.append(prestamo)         # Agregar el préstamo a la lista de préstamos del cliente
        self.saldo += monto                     # Actualizar el saldo del cliente sumando el monto del préstamo
        return prestamo

