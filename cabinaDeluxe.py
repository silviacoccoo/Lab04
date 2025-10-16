"""Creo una sottoclasse per le cabine deluxe"""
from cabina import Cabina

class CabinaDeluxe(Cabina):
    def __init__(self, cod_cab, num_letti, ponte, prezzo, tipo):
        super().__init__(cod_cab, num_letti, ponte, prezzo)
        self.tipo = tipo

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str},tipo={self.tipo}"

    def __repr__(self):
        base_str = super().__repr__()
        return f"{base_str},tipo={self.tipo}"