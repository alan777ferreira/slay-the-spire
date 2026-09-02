from card import Card
from typing import Self


class Entity:
    def __init__(self, name: str, life: int, deck: list[Card], shield: int):
        self.name = name
        self.life = life
        self.deck = deck
        self.shield = shield
        self.weak = 0
        self.vulnerable = 0

    def hit(self, card: Card, target: Self ):
        vulnerable_modifier = 1 + (int(bool(target.vulnerable)) * 0.5)
        target.life -= (card.damage * vulnerable_modifier) - target.shield
        target.vulnerable += card.vulnerable
