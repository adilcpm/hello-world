import random

suits = ['Clubs','Diamonds','Hearts','Spades']
ranks = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True
class Cards():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"
class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Cards(suit,rank))

    def __str__(self):
        deck_comp = ''
        for item in self.deck:
            deck_comp += "\n" + item.__str__
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        #from deck
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
class Chips:
    def __init__(self,total=0):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
def take_bet():
    try:
        bet = int(input("Enter your bet : "))
        if bet > chips.total:
            print("Insufficient funds, try again !")
            take_bet()
        else:
            chips.bet = bet
    except ValueError:
        print("Enter a number : ")
        take_bet()
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
def hit_or_stand(deck,hand):
    global playing
    check = int(input("Hit or Stand ? : 1 for Hit, 2 for Stand "))
    if check == 1:
        hit(deck,hand)
    elif check == 2:
        playing == False
def show_all(player,dealer):
    print("\n\n-----------------------\n")
    print("Dealer's Cards")
    index = 1
    for item in dealer.cards:
        print(f"\t{index}. {item.__str__()}")
        index += 1
    print("\n\nPlayer's Cards")
    index = 1
    for item in player.cards:
        print(f"\t{index}. {item.__str__()}")
        index += 1
    print("-----------------------")
def show_some(player,dealer):
    print("\n\n-----------------------\n")
    print("Dealer's Cards")
    index = 1
    for item in dealer.cards:
        if index == 1:
            print(f"\t{index}. Card Hidden ")
            index += 1
            continue
        print(f"\t{index}. {item.__str__()}")
        index += 1
    print("\n\nPlayer's Cards")
    index = 1
    for item in player.cards:
        print(f"\t{index}. {item.__str__()}")
        index += 1
    print("-----------------------")
def player_busts():
    print("Player Busted !")
    dealer_wins()
def player_wins():
    print("Player Win !")
    chips.win_bet()
def dealer_busts():
    print("Dealer Busted !")
    player_wins()
def dealer_wins():
    print("Dealer Win !")
    chips.lose_bet()
print("\n\n\n\n\n\n\nWelcome to the Blackjack Game !")
chips = Chips()
chips.total = int(input("\n\nEnter your Bank Balance : "))
while True:
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    print("\n"*10)
    take_bet()
    # show_some(player,dealer)
    newindex = 1
    while playing:
        if newindex == 1:
            show_some(player,dealer)
        else:
            show_all(player,dealer)
        hit_or_stand(deck,player)
        if player.value > 21:
            player_busts()
            break
        elif player.value == 21:
            player_wins()
            break
        while dealer.value <= 17:
            hit(deck,dealer)
            show_all(player,dealer)
        if dealer.value > 21:
            dealer_busts()
            break
        elif dealer.value == 21:
            dealer_wins()
            break
        newindex += 1
    print(f"\n\nYour Remaining Bank Balance : {chips.total}")
    check = input("Do you want to bet again? : Y for Yes N for No ").upper()
    if check == "Y":
        continue
    else:
        break
print("Thank you for playing !")
    
   


