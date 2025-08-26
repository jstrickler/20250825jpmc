from card import Card
from carddeck import CardDeck

class Game:
    def play(self):
        print("playing...")

class JokerDeck(Game, CardDeck):
    foo = 5
    def _make_deck(self):
        foo = "wombat"  #local
        self.foo = 25  #instance
        JokerDeck.foo = 10  # class will search JokerDeck MRO
        super()._make_deck()
        for joker_number in 1, 2:
            card = Card(f"Joker-{joker_number}", "*** JOKER ***")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(f"{j.cards = }")
    print(j)
    print(repr(j))
    j.play()
    print(JokerDeck.mro())