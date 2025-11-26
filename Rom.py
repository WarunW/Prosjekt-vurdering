class Rom:
    def __init__(self, navn: str, beskrivelse: str):
        self._navn = navn
        self._beskrivelse = beskrivelse
        self._gjenstander = []
        self._fiende = 
        self.utganger = []   


    def navn(self):
        return self._navn

    def beskrivelse(self):
        return self._beskrivelse

    def leggTilGjenstander(self, gjenstander):
        for g in gjenstander:
            self._gjenstander.append(g)

    def settFiende(self, fiende):
        self._fiende = fiende

    def hentFiende(self):
        return self._fiende

    def hentGjenstander(self):
        return self._gjenstander

    def leggTilUtgang(self, retning: str, rom: "Rom"):
        self.utganger.append((retning, rom))