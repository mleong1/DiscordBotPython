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
        if self.rank == 1:
            return "Ace of " + self.suit
        elif self.rank == 11:
            return "Jack of " + self.suit
        elif self.rank == 12:
            return "Queen of " + self.suit
        elif self.rank == 13:
            return "King of " + self.suit
        else:
            return str(self.rank) + " of " + self.suit

    def __lt__(self, other):
        return self.rank < other.rank
    
class deck:
    cards = []
    def __init__(self):
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for rank in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                         11, 12, 13]:
                self.cards.append(TexasHoldEmCard(rank, suit))

    def peek(self):
        print (self.cards[0])

    def shuffle(self):
        random.shuffle(self.cards)

    def dealCard(self):
        return self.cards.pop(0)

class player:
    money = 100
    folded = False
    
    def __init__(self, name):
        self.name = name
        self.hand = []

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

    def hasFolded(self):
        self.folded = True

    def __str__(self):
        return self.name

class TexasHoldEmGame:
    deck = deck()
    players = []
    
    
    def __init__(self, numOfPlayers):
        #Sets up the deck and the players 
        self.deck.shuffle()
        self.commonCards = []
        for num in range(numOfPlayers):
            self.players.append(player("Player " + str(num)))

    
    def placeInitialBet(self):
        smallBlind = 0
        bigBlind = 1
        self.players[smallBlind].bet(5)
        self.players[bigBlind].bet(10)
        
        if smallBlind < len(self.players):
            smallBlind += 1
        else:
            smallBlind = 0

        if bigBlind < len(self.players):
            bigBlind += 1
        else:
            bigBlind = 0

    def doPlayerAction(self, player, action):
        if action == "check":
            #No bet
            print("no bet")
        elif action == "bet":
            print("How much are we betting?")
        elif action == "fold":
            player.hasFolded()

    def dealHandCards(self):
        for num in range(2):
            for player in self.players:
                card = self.deck.dealCard()
                player.hand.append(card)

    def dealFlop(self):
        self.deck.dealCard()
        for num in range(3):
            card = self.deck.dealCard()
            self.commonCards.append(card)


class evaluator:

    def __init__(self, playerHand, flop):
        self.rankCounter = [13]
        self.suitCounter = [4]
        self.wholeHand = []
        for card in playerHand:
            self.wholeHand.append(card)
        for card in flop:
            self.wholeHand.append(card)
        self.wholeHand.sort()
        
    def isRoyalFlush(self):
        for card in self.wholeHand:
            print(card)
        
        

    

    
        
            
        
        
    
            
