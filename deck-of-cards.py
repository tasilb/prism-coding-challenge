import random

class DeckOfCards:
    def __init__(self):
        # Initialize a list of all cards to be used for shuffling purposes
        self.allCards = [(rank, suit) 
                for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
                for suit in ['club', 'diamond', 'heart', 'spade']]
        random.shuffle(self.allCards)

        # Initialize the deck of cards that gets drawn from
        self.deck = self.allCards[:]

    def shuffle(self):
        random.shuffle(self.allCards)
        self.deck = self.allCards[:] # All cards are put back in the deck, so I only need to shuffle the list of all cards

    def getNextCard(self):
        if len(self.deck) != 0:
            return self.deck.pop()
        else:
            print("No cards are left in the deck--shuffle the deck to continue drawing")

    def cardRank(self, card):
        return card[0]

    def cardSuit(self, card):
        return card[1]
