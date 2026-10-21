import random
from battle import Battle
from card import Card
from entity import Entity

STRIKE_FACTORY = lambda: Card(mana=1, damage=6, name="Strike", type_="Attack")
SHIELD_FACTORY = lambda: Card(mana=1, shield=5, name="Defend", type_="Skill")
deck = [
    STRIKE_FACTORY(),
    STRIKE_FACTORY(),
    STRIKE_FACTORY(),
    STRIKE_FACTORY(),
    SHIELD_FACTORY(),
    SHIELD_FACTORY(),
    SHIELD_FACTORY(),
    SHIELD_FACTORY(),
    Card(mana=2, damage=10, name="Bash", type_="Attack", vulnerable=2),
]
rng = random.Random(42)
rng.shuffle(deck)
monster_deck = [
    Card(mana=0, damage=5, name="Card Monster", type_="Attack"),
]
player = Entity(name="Player", life=100, deck=deck)
monster = Entity(name="Monster", life=100, deck=monster_deck)
battle = Battle(player=player, enemy=monster)

battle.start()