import csv
from cabina import Cabina
from cabinaDeluxe import CabinaDeluxe
from cabinaPetFriendly import CabinaPetFriendly
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""

        # inizializzo l'attributo
        self._nome = nome

        # inizializzo le strutture dati
        self.cabine = {}
        self.passeggeri={}

    def __str__(self): # per stampare una versione leggibile
        return (f"{self.nome}"
                f"{len(self.cabine)} cabine, {len(self.passeggeri)} passeggeri") # la lunghezza dei dizionari indica quante cabine e quanti passeggeri ci sono in una crociera

    def __repr__(self): # stamapa per il debug
        return (f"{type(self).__name__}"
                f"nome={self.nome}")

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, "r", newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for riga in reader:
                        if riga: #verifichiamo che la riga esista, non sia vuota
                            if riga[0].startswith('CAB'):
                                cod_cab=riga[0]
                                num_letti=int(riga[1])
                                ponte=riga[2]
                                prezzo=int(riga[3])

                                if riga[4]=='<unset>':
                                    cabina=Cabina(cod_cab, num_letti, ponte, prezzo) # creo oggetto
                                    self.cabine[cod_cab] = cabina # aggiungo al dizionario con chiave cod_cab
                                else:
                                    if riga[4].isalpha(): # se tutti i caratteri sono lettere
                                        tipo=riga[4]
                                        cabina1=CabinaDeluxe(cod_cab, num_letti, ponte, prezzo, tipo)
                                        self.cabine[cod_cab] = cabina1
                                    else: # se riga[4].isnumeric()
                                        animali=int(riga[4])
                                        cabina2=CabinaPetFriendly(cod_cab, num_letti, ponte, prezzo, animali)
                                        self.cabine[cod_cab] = cabina2
                            elif riga[0].startswith('P'):
                                cod_pass=riga[0]
                                nome=riga[1]
                                cognome=riga[2]

                                passeggero=Passeggero(cod_pass, nome, cognome) # creo oggetto passeggero
                                self.passeggeri[cod_pass]=passeggero # aggiungo al dizionario
        except FileNotFoundError:
            print("File non trovato")
        # TODO

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""

        # verifichiamo che la cabina e il passeggero esistano
        if codice_cabina not in self.cabine:
            raise ValueError("Cabina non trovato")
        if codice_passeggero not in self.passeggeri:
            raise ValueError("Passeggeri non trovato")

        cabina=self.cabine[codice_cabina] # prendo l'oggetto cabina
        passeggero=self.passeggeri[codice_passeggero] # prendo l'oggetto passeggero


        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

