"""Creo una sottoclasse per le cabine che ammettono animali"""
from cabina import Cabina
class CabinaPetFriendly(Cabina): # con questa sintassi si crea una classe figlia CabinaPetFriendly della classe padre Cabina
    def __init__(self, cod_cab, num_letti, ponte, prezzo, num_animali):
        prezzo_finale= prezzo*(1+0.1*num_animali)
        super().__init__(cod_cab, num_letti, ponte, prezzo_finale) # aggiungo gli attributi ereditati dalla classe padre
        self.num_animali = num_animali # aggiungo l'attributo specifico per questa sottoclasse

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} ({self.num_animali})"

    def __repr__(self):
        base_str = super().__repr__()
        return f"{base_str},animali={self.num_animali}"