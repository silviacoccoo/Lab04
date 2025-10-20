"""Creo una sottoclasse per le cabine deluxe"""
from cabina import Cabina

class CabinaDeluxe(Cabina):
    def __init__(self, cod_cab, num_letti, ponte, prezzo, tipo):
        # voglio sostituire il prezzo base con il prezzo maggiorato
        prezzo_finale= prezzo*1.20 # definisco la variabile che contiene il prezzo maggiorato
        super().__init__(cod_cab, num_letti, ponte, prezzo_finale) # sostituisco all'attributo prezzo della classe padre il prezzo_finale, specifico per questa sottoclasse
        self.tipo = tipo # aggiungo l'attributo tipo

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str},tipologia {self.tipo}"

    def __repr__(self):
        base_str = super().__repr__()
        return f"{base_str},tipo={self.tipo}"