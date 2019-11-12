import random

playagain = ()
youwon = 0
youlose = 0
wallet = 100
score = 0
# deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

hand = []
cards = []
hash = {
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 1
}
bet = []
dealer = []


def dealplayer(deck):
    cards = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11: card = hash["J"]
        if card == 12: card = hash["Q"]
        if card == 13: card = hash["K"]
        if card == 14: card = hash["A"]
        hand.append(card)
        cards.append(card)

    print(f"you received {hand[0]} and {hand[1]}")
    print(f"your hand totals {sum(hand)}")


def dealhouse(deck):
    for i in range(2):
        card = deck.pop()

        if card == 11: card = hash["J"]
        if card == 12: card = hash["Q"]
        if card == 13: card = hash["K"]
        if card == 14: card = hash["A"]
        dealer.append(card)
    print(f"The dealer shows {card}")


# print(f"Your current hand is {sum(hand)} and the dealer has {dealer[1]} showing, would you like to hit again?\n)
# print(f"1. Yes \n 2. No \n")
# hitinput=input()
# hitinput = input(f"Your current hand is {sum(hand)} and the dealer has {dealer[1]} showing, would you like to hit again?\n 1. Yes \n 2. No \n")

def hit(deck):
    global youwon
    global youlose
    global playagain
    hitinput = input("\nWould you like to hit?\n1. Yes\n2. No \n")
    print(hitinput)
    while hitinput == "1" or hitinput == "yes":
        card = deck.pop()
        if card == 11: card = hash["J"]
        if card == 12: card = hash["Q"]
        if card == 13: card = hash["K"]
        if card == 14: card = hash["A"]
        hand.append(card)
        cards.append(card)
        print(f"You received a {card}")
        print(f"Your current hand is {sum(hand)} and the dealer has {dealer[1]} showing.\n")
        if sum(hand) > 21: print("Oh no! You have busted!\n")
        youlose = youlose + 1
        if sum(hand) > 21: break
        hitinput = input("\nWould you like to hit?\n1. Yes\n2. No \n")
    if hitinput != "1" or hitinput != "yes":
        print(f"The dealer flips over their card revealing {dealer}!")
        while sum(hand) > sum(dealer) and sum(hand) < 22:
            card = deck.pop()
            if card == 11: card = hash["J"]
            if card == 12: card = hash["Q"]
            if card == 13: card = hash["K"]
            if card == 14: card = hash["A"]
            dealer.append(card)
            print(f"The dealer drew a {card}, totaling {sum(dealer)}")
            if sum(dealer) > 21: print("Dealer has busted, you win!")
            youwon = youwon + 1
        if sum(hand) > 21 and sum(dealer) > 21:
            print("you have busted\n")
            youlose = youlose + 1
        if sum(dealer) >= sum(hand) and sum(dealer) < 22:
            print("you have lost to the dealer\n")
            youlose = youlose + 1
        if sum(hand) > sum(dealer) and sum(hand) < 22:
            print("you have won!")
            youwon = youwon + 1
            print(f"You had {sum(hand)} and the dealer had {sum(dealer)}")
    playagain = input("\nWould you like to play again?\n")


dealplayer(deck)
dealhouse(deck)
hit(deck)
while playagain == "yes" or playagain == "Yes":
    print(f"You have lost {youlose} times and won {youwon} times")
    score = 0
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
    hand = []
    cards = []
    hash = {
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 1
    }
    bet = []
    dealer = []
    dealplayer(deck)
    dealhouse(deck)
    hit(deck)

else:
    print("Thanks for playing!")