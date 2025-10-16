import csv

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""

        self.nome = nome # attributo della nave

        # inizializzo le strutture dati
        self.cabine = {}
        self.passeggeri={}

    def __str__(self): # per stampare una versione leggibile
        return f"{self.nome}"

    """Aggiungere setter e getter se necessari"""

    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, "r", newline='', encoding='utf-8') as file:
                reader = csv.reader(file)

                for riga in reader:
                        if riga: #verifichiamo che la riga esista, non sia vuota
                            if riga[0].startswith('CAB'):
                                pass
                            elif riga[0].startswith('P'):
                                pass
        except FileNotFoundError:
            print("File non trovato")
        # TODO

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

