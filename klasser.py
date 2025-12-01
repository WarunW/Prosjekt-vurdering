class Item:
    def __init__(self, navn: str, beskrivelse: str):
        self._navn = navn
        self._beskrivelse = beskrivelse

    def useItem(self, spiller):
        print(f"Du kan ikke bruke {self._navn} på den måten")

class AccessCard(Item):
    def __init__(self):
        super().__init__("kodekort", "Et kodekort som kan åpne bankhvelvet.")
        
    def useItem(self, spiller):
        for retning, rom in spiller._rom.utganger:
            if retning == "hvelv" and rom.erLåst():
                rom.låsOpp()
                print("Du bruker kodekortet og låser opp hvelvdøren.")
                return
        print("Det er ingen låst bankdør her.")

class EnergyBar(Item):
    def __init__(self, healAmount: int = 3):
        super().__init__("energibar", "Gir deg litt mer HP når du spiser den.")
        self._healAmount = healAmount

    def useItem(self, spiller):
        spiller._hp += self._healAmount
        print(f"Du spiser en energibar og får + {self._healAmount} HP.")
        print(f"Du har nå {spiller._hp} HP")

class Inventar:
    def __init__(self):
        self._items: list[Item] = []

    def addItem(self, item: Item):
        self._items.append(item)

    def removeItem(self, item: Item):
        if item in self._items:
            self._items.remove(item)

    def hasItem(self, navn: str):
        for item in self._items:
            if item._navn == navn:
                return True
        return False
        
    def getItem(self, navn: str):
        for i in self._items:
            if i._navn == navn:
                return i
        return None
    
    def listItem(self):
        if not self._items:
            print("Inventaret ditt er tomt.")
        else:
            print("Du har:")
            for i in self._items:
                print(f"- {i._navn}: {i._beskrivelse}")

class Spiller:
    def __init__(self, navn: str):
        self._navn = navn
        self._hp = 10
        self._inventar = Inventar()
        self._rom = None

    def settRom(self, rom):
        self._rom = rom

    def attack(self, fiende: "Fiende"):
        damage = 2
        fiende.takeDamage(damage)
        print(f"Du angriper {fiende._navn} og gjør {damage} skade.")

    def takeDamage(self, amount: int):
        self._hp -= amount
        print(f"{self._navn} tar {amount} skade. Hp: {self._hp}")

    def useItem(self, item_name: str):
        item = self._inventar.getItem(item_name)
        if item:
            item.useItem(self)
            if isinstance(item, EnergyBar):
                self._inventar.removeItem(item)
        else:
            print(f"Du har ikke {item_name}.")

class Fiende:
    def __init__(self, navn:str, skade: int):
        self._navn = navn
        self._hp = 5
        self._skade = skade

    def attack(self, spiller: Spiller):
        print(f"{self._navn} angriper deg!")
        spiller.takeDamage(self._skade)

    def takeDamage(self, amount: int):
        self._hp -= amount
        print(f"{self._navn} tar {amount} skade. Hp: {self._hp}")

    def is_alive(self):
        alive = self._hp > 0
        if alive:
            print("Fienden lever!")
        else:
            print("Fienden er død!")
        return alive

class Sikkerhetsvakt(Fiende):
    def __init__(self):
        super().__init__("sikkerhetsvakt", skade = 2)