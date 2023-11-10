import datetime


class Prestamo:
    def __init__(self, monto, fecha, cliente):
        self.monto = float(monto)
        self.fecha = fecha
        self.fecha_final = self.fecha + datetime.timedelta(days=24)
        self.cliente = cliente
        self.monto_pagado = 0     
    
    def tasa_interes(self):
        """Devuelve la tasa de interés del préstamo."""
        return 0.2
    
    def obtener_estado(self):
        """Devuelve un diccionario con el estado del préstamo, el monto cobrado, el monto diario, el estado de pago y la fecha de vencimiento."""
        monto_cobrado = self.monto * (1 + self.tasa_interes())
        monto_diario = round((monto_cobrado / 24), 2)
        fecha_vencimiento = self.fecha + datetime.timedelta(days=24)
        estado_pago = "Pagado" if self.monto_pagado == self.monto else "Atrasado" if datetime.date.today() > fecha_vencimiento else "Al día"
        return "\n".join(
            [
                f"- Monto a pagar en 24 días: {round((monto_cobrado),2)}",                
                f"- Monto diario: {monto_diario}",
                f"- Estado de pago: {estado_pago}",
                f"- Fecha de vencimiento: {fecha_vencimiento}",
            ]
        )






