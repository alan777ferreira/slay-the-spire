from typing import Self


class Card:
    def __init__(self, mana, damage, name, shield, type_):
        self.mana = mana
        self.damage = damage
        self.shield = shield
        self.name = name
        self.type_ = type_

    def __str__(self) -> str:
        return f"{self.name}"


class Entity:
    def __init__(self, name: str, life: int, deck: list[Card], shield: int):
        self.name = name
        self.life = life
        self.deck = deck
        self.shield = shield
        self.weak = 0
        self.vulnerable = 0

    def hit(self, damage, target: Self):
        vulnerable_modifier = 1
        # vulnerable_modifier = 1 + (int(target.is_vulnerable) * 0.5) - (self.is_weak * (2/3))
        target.life -= (damage * vulnerable_modifier) - target.shield



def player_turn(player: Entity, monster: Entity, deck: list[Card]):
    print(f"Player ({player.life}) - Monster ({monster.life})")
    print("What do you want to do?")
    for card_number, card in enumerate(deck):
        print(f"{card_number} -- ({card})")

    try:
        decision = int(input())
    except (TypeError, ValueError):
        print("Invalid command, chosing first card")
        decision = 0
    card_chosen = deck[decision]
    if card_chosen.type_ == "Attack":
        monster.life -= card_chosen.damage
    if card_chosen.type_ == "Skill":
        player.shield += card_chosen.shield

deck = [
    Card(mana=1, damage=6, shield=0, name="Strike", type_="Attack"),
    Card(mana=1, damage=0, shield=5, name="Defend", type_="Skill"),
]
player = Entity(name="Player", life=100, deck=deck, shield=0)
monster = Entity(name="Monster", life=100, deck=[], shield=0)
def turno(index: int):
    print(f"Turno: {index}")

    # turn_reset
    entities = [player, monster]

    for entity in entities:
        entity.shield = 0
        if entity.weak:
            entity.weak -= 1
        if entity.vulnerable:
            entity.vulnerable -= 1

    player_turn(player=player, monster=monster, deck=deck)
    print("*" * 50)
    # monster turn
    monster.hit(damage=5, target=player)

turn = 1
while player.life > 0 and monster.life > 0:
    turno(turn)
    turn += 1

if player.life > 0:
    vencedor = player.name
elif monster.life > 0:
    vencedor = monster.name
else:
    vencedor = "Empate"

print(f"Vencedor: {vencedor}")