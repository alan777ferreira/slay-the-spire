from card import Card
from entity import Entity


class Battle:
    def __init__(self, player: Entity, enemy: Entity):
        self.draw_pile = player.deck
        self.discard_pile = []
        self.exhaust_pile = []
        self.turn = 1
        self.player = player
        self.enemy = enemy
    def draw_card(self) -> Card:
        if not self.draw_pile:
            while self.discard_pile:
                self.draw_pile.append(self.discard_pile.pop())
        return self.draw_pile.pop()


    def player_turn(self):
        hand = []
        while len(hand) <= 5:
            hand.append(self.draw_card())

        mana = 3
        print(f"Player's mana({mana})")
        print(f"Player ({self.player.life}) - Monster ({self.enemy.life}, {self.enemy.vulnerable})")
        print("What do you want to do?")
        for card_number, card in enumerate(hand):
            print(f"{card_number} -- ({card})")

        try:
            decision = int(input())
        except (TypeError, ValueError):
            print("Invalid command, chosing first card")
            decision = 0
        card_chosen = hand[decision]
        if card_chosen.mana > mana:
            print("You don't have enough mana")
        else:
            if card_chosen.type_ == "Attack":
                self.player.hit(card=card_chosen, target=self.enemy)
                mana -= card_chosen.mana
            if card_chosen.type_ == "Skill":
                self.player.shield += card_chosen.shield
                mana -= card_chosen.mana
        while hand:
            self.discard_pile.append(hand.pop())

    def turno(self):
        print(f"Turno: {self.turn}")

        # turn_reset
        entities = [self.player, self.enemy]
        for entity in entities:
            entity.shield = 0
            if entity.weak:
                entity.weak -= 1
            if entity.vulnerable:
                entity.vulnerable -= 1
        self.player_turn()

        print("*" * 50)
        # monster turn
        self.enemy.hit(card=self.enemy.deck[0], target=self.player)

    def start(self) -> str:
        while self.player.life > 0 and self.enemy.life > 0:
            self.turno()
            self.turn += 1

        if self.player.life > 0:
            vencedor = self.player.name
        elif self.enemy.life > 0:
            vencedor = self.enemy.name
        else:
            vencedor = "Empate"

        return vencedor