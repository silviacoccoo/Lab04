"""Creo una sottoclasse per le cabine deluxe."""
from cabina import Cabina

class CabinaDeluxe(Cabina):
    def __init__(self, cod_cab, num_letti, ponte, prezzo, tipo):

        # voglio sostituire il prezzo base con il prezzo maggiorato
        prezzo_base=float(prezzo)
        prezzo_finale= prezzo_base*1.20 # definisco la variabile che contiene il prezzo maggiorato

        super().__init__(cod_cab, num_letti, ponte, prezzo_finale) # sostituisco all'attributo prezzo della classe padre il prezzo_finale, specifico per questa sottoclasse

        self.tipo = tipo # aggiungo l'attributo tipo
        self.prezzo_base = prezzo_base

    def __str__(self):
        stato='Disponibile' if self.disponibile else f'Occupata dal passeggero {self.passeggero_associato}'
        return (f"Cabina {self.cod_cab}: "
                f"{self.num_letti} letti, ponte {self.ponte}, prezzo {self.prezzo}, tipologia {self.tipo} - Stato: {stato}")

    def __repr__(self):
        return (f"Cabina {type(self).__name__}: "
                f"(cod_cab={self.cod_cab}, letti={self.num_letti}, ponte={self.ponte}, prezzo={self.prezzo:.2f}, tipo={self.tipo})")