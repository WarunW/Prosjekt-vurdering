class Spiller:
    def __init__(self, navn: str, hp: int):
        self.navn = navn
        self.hp = hp
        # self.inventar = inventar()

    def attack(self, fiende: "Fiende"):
        damage = 2
        fiende.takeDamage(damage)
        print(f"Du angriper {fiende.navn} og gjør {damage} skade.")

    def takeDamage(self, amount: int):
        self.hp -= amount
        print(f"{self.navn} tar {amount} skade. Hp: {self.hp}")

    def useItem(self, item_name: str):
        item = self.inventar.getItem(item_name)
        if item:
            item.useItem(self)
            if isinstance(item, EnergyBar):
                self.inventar.removeItem(item)
        else:
            print(f"Du har ikke {item_name}.")