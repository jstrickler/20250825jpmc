class Card:  # object.__init__()
    # rank, suit
    def __init__(self, rank_in: str, suit_in: str):
        self.rank = rank_in
        self.suit = suit_in

    @property
    def rank(self):  # getter property
        return self._rank
    # rank = property(rank)

    @rank.setter
    def rank(self, value):  #setter property
        if isinstance(value, str):
            self._rank = value
        else:
            raise TypeError("rank must be a str")
        
    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, new_value):   # obj.prop = new_value
        if isinstance(new_value, str):
            self._suit = new_value
        else:
            raise TypeError("suit value must be a str")

    def __str__(self):
        return f"Card:{self.rank}/{self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card("8", "Diamonds")
    print(f"{c1.rank = }")
    print(f"{c1.suit = }")
    c1.suit = "Clubs"
    print(f"{c1.suit = }")
    print(c1)  # print(str(c1))
    print(f"{c1 = }")
    print(f"c1 = {c1}")
    c2 = Card("Jack", "Hearts")
    print(f"{c2.rank = }")
    

