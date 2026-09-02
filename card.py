class Card:
    def __init__(self, mana, damage, name, shield, type_, vulnerable):
        self.mana = mana
        self.damage = damage
        self.shield = shield
        self.name = name
        self.type_ = type_
        self.vulnerable = vulnerable

    def __str__(self) -> str:
        return f"{self.name}"
