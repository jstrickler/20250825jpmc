import random
from card import Card

class CardDeck:
    """
    One deck of cards

    USAGE:
        d = CardDeck()
        d.shuffle()
        card = d.draw()
    """
    SUITS = "Clubs Diamonds Hearts Spades".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self):
        self._make_deck()
    
    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:  # CardDeck.SUITS
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)
    
    @property
    def cards(self):
        return tuple(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __len__(self):  # implements len()
        return len(self._cards)
    
    def __add__(self, other):
        new_deck = type(self)()
        new_deck._cards = self._cards + list(other.cards)
        return new_deck

    def __repr__(self):
        my_name = type(self).__name__
        return f"{my_name}()"

    # instance method
    def __str__(self):
        my_name = type(self).__name__
        return f"{my_name}:{len(self)}"
    
    @classmethod
    def get_suits(cls):
        return cls.SUITS

    @staticmethod
    def double(x):
        return 2 * x

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    d1.shuffle()    
    print(f"{d1.cards = }")
    for _ in range(5):
        print(d1.draw())
    print(len(d1))   # d1.__len__()

    d3 = d1 + d2
    print(f"{len(d3) = }")
    print(f"{d1 = }")
    print(f"{d1 = !s}")
    print(f"{d1.get_suits() = }")
    print(f"{CardDeck.get_suits() = }")
    
# print(dir(object))