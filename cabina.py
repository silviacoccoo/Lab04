"""Creo la classe principale per la Cabina"""
class Cabina:
    def __init__(self, cod_cab, num_letti: int, ponte, prezzo: float):
        self.cod_cab = cod_cab
        self.num_letti = int(num_letti)
        self.ponte = ponte
        self.prezzo = float(prezzo)

        self.disponibile=True
        self.passeggero_associato=None

    def __str__(self): # metodo di visualizzazione leggibile
        stato='Disponibile' if self.disponibile else f'Occupata dal passeggero {self.passeggero_associato}'
        return (f"Cabina {self.cod_cab}: "
                f"{self.num_letti} letti, ponte {self.ponte}, prezzo {self.prezzo: .2f} - Stato: {stato}")

    def __repr__(self):
        return (f"Cabina {type(self).__name__}: "
                f"(cod_cab={self.cod_cab}, letti={self.num_letti}, ponte={self.ponte}, prezzo={self.prezzo})")