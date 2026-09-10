from card import Card
from entity import Entity


def test_enemy():
    player = Entity("player", 10, [
        Card(mana=1, damage=6, shield=0, name="Strike", type_="Attack", vulnerable=0)
    ], 0)
    enemy = Entity("monster", 10, [
        Card(mana=0, damage=5, name="Card Monster", shield=0, type_="Attack", vulnerable=0)
    ], 0)
    player.hit(card=player.deck[0], target=enemy)
    assert enemy.life == 4, "A soma não bateu"



def soma(a, b):
    return a + b

def test_soma():
    assert soma(10, 20) == 30, "A soma não bateu"

def test_soma_string():
    assert soma("a", "b") == "ab", "A soma não bateu"


