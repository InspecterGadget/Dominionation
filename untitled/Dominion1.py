__author__ = 'stevenkerr'
import random

class Deck():
    def __init__(self):
        """ self represents the object that is being created"""
        self.size = 10
        self.coppers = 7
        self.estates = 3
class Discard():
    def __init__(self):
        """ self represents the object that is being created"""
        self.size = 14
        self.coppers =9
        self.estates = 5
        self.silvers = 0

#deck = Deck()

class Copper():
    def __init__(self):
       self.cost = 0
       self.tresure = 1
       self.action = False
       self.draw_cards = 0
       self.gain_actions = 0
       self.victory = 0

class Estate():
    def __init__(self):
        self.cost = 2
        self.tresure = 0
        self.action = False
        self.draw_cards = 0
        self.gain_actions = 0
        self.victory = 1

class Silver():
    def __init__(self):
        self.cost = 3
        self.tresure = 2
        self.action = False
        self.draw_cards = 0
        self.gain_actions = 0
        self.victory = 0

def post_draw(deck,card):
    deck.size -= 1
    if card == 'Copper':
            deck.coppers -= 1
    elif card == 'Estate':
        deck.estates -= 1
    elif card == 'Silver':
        deck.silvers -= 1
    else:
        raise ValueError
        return deck

def buy_card(discard, card):
        if card == 'Copper':
             discard.coppers += 1
        elif card == 'Estate':
            discard.estates += 1
        elif card == 'Silver':
            discard.silvers +=1
        else:
            raise ValueError
        return discard


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


def draw_cards(deck, num, discard):
        cards_drawn = []
        for x in range(0,num):
            print "Coppers in deck = ",deck.coppers
            if deck.size == 0:
                deck = discard
            card = draw_card(deck)
            cards_drawn.append(card)
            post_draw(deck,card)
        return cards_drawn
def assign_class(card):
    if card == 'Copper':
             card_type = Copper()
    elif card == 'Estate':
            card_type = Estate()
    elif card == 'Silver':
            card_type = Silver()
    else:
            raise ValueError
    return card_type
def assign_classes(card_list,num):
    card_class_list = []
    for x in range(0,num):
        card_class_list.append(assign_class(card_list[x]))
    return card_class_list
def post_play_pile_shift(deck,hand,num,discard):
    for x in range(0,num):
        card = hand[x]
        post_draw(deck,card)
    for x in range(0,num):
        card = hand[x]
        buy_card(discard,card)

deck = Deck()
discard = Discard()
deck = discard
draw_cards(deck,5,discard)

#post_play_pile_shift(deck,hand,5,discard)
print deck.coppers
print discard.coppers

"""
print deck.estates
print deck.coppers
hand = draw_cards(deck, 5,discard)
print hand
print deck.estates
print deck.coppers
hand = draw_cards(deck, 5,discard)
print hand
print deck.estates
print deck.coppers
hand = draw_cards(deck, 5,discard)
print hand
print deck.size
print deck.coppers

#print work_hand
#first_card = work_hand[0]
#print first_card.cost"""