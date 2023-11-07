import pickle
from ClassPrestamo import * 

class Cliente:
    def __init__(self, nombre, cedula, saldo):
        self.nombre = nombre
        self.cedula = cedula
        self.saldo = saldo
        self.prestamos = []  # lista para guardar los préstamos

    def solicitar_prestamo(self, monto, fecha):
        """Crea un nuevo préstamo para el cliente y lo agrega a la lista de préstamos."""
        prestamo = Prestamo(monto, fecha, self)
        self.prestamos.append(prestamo)
        self.saldo += monto
        return prestamo
