"""Creo una sottoclasse per le cabine che ammettono animali."""
from cabina import Cabina
class CabinaPetFriendly(Cabina): # con questa sintassi si crea una classe figlia CabinaPetFriendly della classe padre Cabina
    def __init__(self, cod_cab, num_letti, ponte, prezzo, num_animali):

        prezzo_base=float(prezzo)
        prezzo_finale= prezzo_base*(1+0.1*num_animali)

        super().__init__(cod_cab, num_letti, ponte, prezzo_finale) # aggiungo gli attributi ereditati dalla classe padre

        self.num_animali = num_animali # aggiungo l'attributo specifico per questa sottoclasse
        self.prezzo_base = prezzo_base

    def __str__(self):
        stato='Disponibile' if self.disponibile else f'Occupata dal passeggero {self.passeggero_associato}'
        return (f"Cabina {self.cod_cab}: "
                f"{self.num_letti} letti, ponte {self.ponte}, prezzo {self.prezzo:.2f}, {self.num_animali} - Stato: {stato}")

    def __repr__(self):
        return (f"Cabina {type(self).__name__}:"
                f"(cod_cab={self.cod_cab}, letti={self.num_letti}, ponte={self.ponte}, prezzo={self.prezzo:.2f}, animali={self.num_animali})")