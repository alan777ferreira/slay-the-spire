class Card:
    def __init__(self, mana, name, type_, vulnerable=0,damage=0, shield=0):
        self.mana = mana
        self.damage = damage
        self.shield = shield
        self.name = name
        self.type_ = type_
        self.vulnerable = vulnerable

    def __str__(self) -> str:
        return f"{self.name}"
