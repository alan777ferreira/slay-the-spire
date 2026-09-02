import random
from battle import Battle
from card import Card
from entity import Entity


deck = [
    Card(mana=1, damage=6, shield=0, name="Strike", type_="Attack", vulnerable=0),
    Card(mana=1, damage=6, shield=0, name="Strike", type_="Attack", vulnerable=0),
    Card(mana=1, damage=6, shield=0, name="Strike", type_="Attack", vulnerable=0),
    Card(mana=1, damage=6, shield=0, name="Strike", type_="Attack", vulnerable=0),
    Card(mana=1, damage=0, shield=5, name="Defend", type_="Skill", vulnerable=0),
    Card(mana=1, damage=0, shield=5, name="Defend", type_="Skill", vulnerable=0),
    Card(mana=1, damage=0, shield=5, name="Defend", type_="Skill", vulnerable=0),
    Card(mana=1, damage=0, shield=5, name="Defend", type_="Skill", vulnerable=0),
    Card(mana=2, damage=10, shield=0, name="Bash", type_="Attack", vulnerable=2),
]
rng = random.Random(42)
rng.shuffle(deck)
monster_deck = [
    Card(mana=0, damage=5, name="Card Monster", shield=0, type_="Attack", vulnerable=0),
]
player = Entity(name="Player", life=100, deck=deck, shield=0)
monster = Entity(name="Monster", life=100, deck=monster_deck, shield=0)
battle = Battle(player=player, enemy=monster)

battle.start()