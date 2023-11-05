import datetime

class Prestamo:
    def __init__(self, monto, fecha, cliente):
        self.monto = monto
        self.fecha = fecha
        self.cliente = cliente
        self.monto_pagado = 0     

    def cantidad_dias(self):
        """Devuelve la cantidad de días que han pasado desde que se solicitó el préstamo."""
        return (datetime.date.today() - self.fecha).days

    def tasa_interes(self):
        """Devuelve la tasa de interés del préstamo."""
        return 0.2

    def calcular_monto_diario(self):
        """Devuelve el monto diario que se debe pagar por el préstamo."""
        return self.monto / 24

    def calcular_monto_total(self):
        """Devuelve el monto total que se debe pagar por el préstamo, incluyendo el interés."""
        return self.monto * (1 + self.tasa_interes())

    def registrar_pago(self, monto):
        """Registra un pago por el préstamo y actualiza el monto pagado."""
        self.monto_pagado += monto

    def obtener_estado(self):
        """Devuelve un diccionario con el estado del préstamo, incluyendo el monto pendiente, el monto diario y la cantidad de días restantes."""
        monto_pendiente = self.monto - self.monto_pagado
        monto_diario = self.calcular_monto_diario()
        cantidad_dias_restantes = (self.cantidad_dias() - self.monto_pagado / monto_diario)
        return {
            "- Monto pendiente": monto_pendiente,
            "- Monto diario": monto_diario,
            "- Cantidad de dias restantes": cantidad_dias_restantes,
        }




