"""Creo una sottoclasse per le cabine che ammettono animali"""
from cabina import Cabina
class CabinaPetFriendly(Cabina): # con questa sintassi si crea una classe figlia CabinaPetFriendly della classe padre Cabina
    def __init__(self, cod_cab, num_letti, ponte, prezzo, num_animali):
        super().__init__(cod_cab, num_letti, ponte, prezzo) # aggiungo gli attributi ereditati dalla classe padre
        self.num_animali = num_animali # aggiungo l'attributo specifico per questa sottoclasse

    def __str__(self):
        pass
