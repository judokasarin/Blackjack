import random
import os

suits = ('hearts','spade','diamond','clubs')
value = {'Jack':10,'Queen':10,'King':10,'Ace':10,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10}
ranks= ('Jack','Queen','King','Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten')

class Cards:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return(f'{self.rank} of {self.suit}')


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Cards(suit,rank))

    
    def __str__(self):
        string_deck = []
        for suit in suits:
            for rank in ranks:
                string_deck.append(str(Cards(suit,rank)))
        return str(string_deck)
        #return str(value[self.deck[1].rank])

    def shuffle(self):
        random.shuffle(self.deck) 

    def deal(self):
        return (self.deck.pop())

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        if card.rank == 'Ace':
            self.adjust_for_ace()
        else:
            self.value = self.value + value[card.rank]
        #print(f'Your hand is now worth the value of {self.value}')

    
    
    def adjust_for_ace(self):
        while True:
            value = int(input('Please enter a what value you want ,1 or 11 : '))
            if value == 1 or value == 11:
                self.value = self.value + value
                break
            else:
                print('Please enter a valid number')
                continue 

class Chips:
    
    def __init__(self):
        self.total = int(input('Please Enter the Number of Chips you want to start with : '))        
        self.bet = 0
        
    def win_bet(self):
        self.total = self.total+self.bet
    
    def lose_bet(self):
        self.total-self.bet


def take_bet():
    bet = int(input('Please enter the bet you want to make : '))


def show_some(player_hand):
        for card in player_hand.cards:
            print(str(card))



deck1 = Deck()
deck1.shuffle()
#print(deck1)
player_card1 = deck1.deal()
player_card2 = deck1.deal()
#card1 = Cards('hearts','Ace')
player_hand = Hand()
player_hand.add_card(player_card1)
player_hand.add_card(player_card2)

show_some(player_hand)



