__author__ = 'stevenkerr'
import random
class Bank:
    def __init__(self):
       self.provinces = 8
       self.duchys = 8
       self.golds = 25
       self.silvers = 40
       self.estates = 8
       self.coppers = 40
#print bank.provinces
class Copper:
    def __init__(self):
       self.cost = 0
       self.treasure = 1
       self.action = False
       self.draw_cards = 0
       self.gain_actions = 0
       self.victory = 0
       self.name = 'Copper'

class Estate:
    def __init__(self):
        self.cost = 2
        self.treasure = 0
        self.action = False
        self.draw_cards = 0
        self.gain_actions = 0
        self.victory = 1
        self.name = 'Estate'

class Silver:
    def __init__(self):
        self.cost = 3
        self.treasure = 2
        self.action = False
        self.draw_cards = 0
        self.gain_actions = 0
        self.victory = 0
        self.name = 'Silver'
class Gold():
    def __init__(self):
        self.cost = 6
        self.treasure = 3
        self.action = False
        self.draw_cards = 0
        self.gain_actions = 0
        self.victory = 0
        self.name = 'Gold'
class Province():
    def __init__(self):
        self.cost = 8
        self.treasure = 0
        self.action = False
        self.draw_cards = 0
        self.gain_actions = 0
        self.victory = 6
        self.name = 'Province'
class Duchy():
    def __init__(self):
        self.cost = 5
        self.treasure = 0
        self.action = False
        self.draw_cards = 0
        self.gain_actions = 0
        self.victory = 3
        self.name = 'Duchy'

class Player:
    def __init__(self):
        self.deck = []
        self.hand = []
        self.discard = []

    def print_deck(self):
        deck_print = []
        for x in range (0,len(self.deck)):
            deck_print.append(self.deck[x].name)
        print deck_print

    def print_hand(self):
        hand_print = []
        for x in range (0,len(self.hand)):
            hand_print.append(self.deck[x].name)
        print hand_print

    def print_discard(self):
        discard_print = []
        for x in range (0,len(self.discard)):
            discard_print.append(self.discard[x].name)
        print discard_print

    def shuffle_discards(self):
        for x in range(0,len(self.discard)):
            self.deck.append(self.discard[x])
        self.discard = []

    def draw_cards(self, num):
        cards_drawn = []
        for x in range(0,num):
            if len(self.deck) == 0:
                self.shuffle_discards()
            card = random.randint(0,len(self.deck)-1)
            card_type = self.deck.pop(card)
            cards_drawn.append(card_type)
        return cards_drawn

    def treasure_count(self):
        count = 0
        for x in range(0,len(self.hand)):
            treasure = self.hand[x].treasure
            count = treasure + count
        return count
    def victory_count(self):
        count = 0
        for x in range(0,len(self.deck)):
            victory_points = self.deck[x].victory
            count = victory_points + count
        for x in range(0,len(self.discard)):
            victory_points = self.discard[x].victory
            count = victory_points + count
        return count
    def buy_strategy(self,t):
        if t >= 8:
            buy = Province()
            bank.provinces -= 1
        elif t >= 6:
            buy = Gold()

        elif t >= 3:
           buy = Silver()
        else:
            buy = Copper()
        return buy
    def discard_hand(self):
        for x in range(0,len(self.hand)):
            self.discard.append(self.hand[x])
        self.hand = []

    def take_turn(self):
        self.hand = self.draw_cards(5)
        treasure = self.treasure_count()
        card_to_buy = self.buy_strategy(treasure)
        self.discard.append(card_to_buy)
        self.discard_hand()

    def play_games(num):
        for x in range(0,num):
            player_one = Player()
            player_two = Player()
            copper = Copper()
            estate = Estate()
            bank = Bank()
            player_one.deck = [copper,copper,copper,copper,copper,copper,copper,estate,estate,estate]
            player_two.deck = [copper,copper,copper,copper,copper,copper,copper,estate,estate,estate]

            print "Rounds played in game ", play_game()
            print "Player one final points ", player_one.victory_count()
            print "Player two final points ", player_two.victory_count()
def play_game():
    total_rounds = 0

    while bank.provinces != 0:
        player_one.take_turn()
        player_two.take_turn()
        total_rounds += 1
    
    return total_rounds





