__author__ = 'stevenkerr'
import random
import decimal

class Pile():
    def __init__(self):
        """ self represents the object that is being created"""
        self.size = 0
        self.estates = 0
        self.coppers = 0
        self.silvers = 0
        self.gold = 0
def create_starting_deck():
    deck = Pile()
    deck.size = 12
    deck.coppers = 7
    deck.estates = 3
    deck.silvers
    return deck

def adjust_deck(deck, card):
    deck.size = deck.size-1
    if card == 'Copper':
             deck.coppers = deck.coppers-1
    elif card == 'Estate':
            deck.estates = deck.estates-1
    elif card == 'Silver':
        deck.silvers = deck.silvers-1
    else:
          card_type = 'Error'
    return deck

def draw_card(deck):
    card = random.randint(1,deck.size)
    if card <= deck.estates:
             card_type = 'Estate'
    elif card <= deck.coppers + deck.estates:
            card_type = 'Copper'
    elif card <= deck.coppers + deck.estates + deck.silvers:
            card_type = 'Silver'
    else:
          card_type = 'Error'
    return card_type
def draw_cards(deck, num):
        cards_drawn = []
        for x in range(0,num):
            if deck.size != 0:
                card = draw_card(deck)
                cards_drawn.append(card)
                adjust_deck(deck,card)
        return cards_drawn

def treasure_counter(hand,num):
    treasure = 0
    for x in range(0,num):
      if hand[x]  == 'Copper':
          treasure += 1
      elif hand[x] == 'Silver':
          treasure += 2
    return treasure


def draw_thousand_hands(deck_one):
    treasure_list = []
    for x in range(0,10):
        treasure_list.append(0)
    for x in range(0,10000):
        deck = create_starting_deck()
        hand = draw_cards(deck,5)
        treasure = treasure_counter(hand,5)
        treasure_list[treasure] += 1
    print treasure_list

def buy_card(discard, card):
        discard.size = discard.size+1
        if card == 'Copper':
             discard.coppers = discard.coppers+1
        elif card == 'Estate':
            discard.estates = discard.estates+1
        else:
              card_type = 'Error'
        return discard

deck = create_starting_deck()
hand = draw_cards(deck,5)
print treasure_counter(hand,len(hand))
print hand

draw_thousand_hands(deck)


