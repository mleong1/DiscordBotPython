import random

class TexasHoldEmCard:

    isAvailable = True
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def setAvailable(self):
        self.isAvailable = True

    def setUnavailable(self):
        self.isAvailable = False
        
    def __str__(self):
        return self.rank + " of " + self.suit
    
class deck:
    cards = []
    def __init__(self):
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for rank in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                        'Jack', 'Queen', 'King']:
                self.cards.append(TexasHoldEmCard(rank, suit))

    def peek(self):
        print (self.cards[0])

    def shuffle(self):
        random.shuffle(self.cards)

    def dealCard(self):
        return self.cards.pop(0)

class player:
    money = 100
    hand = []
    def __init__(self, name):
        self.name = name

    def bet(self, amount):
        if amount < self.money:
            self.money -= amount
            return amount
        else:
            self.allIn()

    def allIn(self):
        bigBet = self.money
        self.money = 0
        return bigBet

class TexasHoldEmGame:
    deck = deck()
    players = []
    
    def __init__(self, numOfPlayers):
        #Sets up the deck and the players 
        self.deck.shuffle()
        for num in range(numOfPlayers):
            self.players.append(player(num))

    
    def initialBet(self):
        
