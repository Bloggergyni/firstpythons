import random
score = 0
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
hand = []
dealer = []
global win
global lose
hash = {
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 1
}
# class deck(self):
#     def __init__(self, cardnumber):
#         self.cardnumber = cardnumber
#     def


def dealplayer(deck, hand):
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

    print(f"you received {cards[0]} and {cards[1]}")
    print(f"your hand is {hand}")



def dealhouse(deck, dealer):
    for i in range(2):
        card = deck.pop()
        if card == 11: card = hash["J"]
        if card == 12: card = hash["Q"]
        if card == 13: card = hash["K"]
        if card == 14: card = hash["A"]
        dealer.append(card)
    print(f"The dealer shows {dealer[0]}")

def hit(deck, hand, dealer):
    hitinput = input("Would like to hit? \n Yes \n No \n")
    while hitinput == "Yes":
        card = deck.pop()
        if card == 11: card = hash["J"]
        if card == 12: card = hash["Q"]
        if card == 13: card = hash["K"]
        if card == 14: card = hash["A"]
        hand.append(card)
        print(f"You received a {card}")
        print(hand, "hand")
        print(dealer, "dealer")
        print(f"Your total is currently {sum(hand)} and the dealer shows {dealer[1]}")
        if sum(hand) > 21:
            print("You bust")
            playagain()
            # lose = lose +1
        if sum(hand) == 21:
            print ("Blackjack!")
            playagain()
        # if sum(hand) > 21:
            # win = win + 1
        hitinput = input("Would like to hit? \n Yes \n No \n")
    if hitinput == "No":
        print(f"The dealer flips his card to reveal {dealer[1]}")
        print(f"The dealers total is now {sum(dealer)}")
        if sum(dealer) >= sum(hand) and sum(dealer) < 22:
            print("The dealer won")
            blah = playagain()
            if not blah:
                return
            # lose = lose + 1
        # print(f"{sum(hand)}")
        # print(f"{sum(dealer)}")
        while sum(dealer) < sum(hand) and sum(hand) < 22:
            if sum(dealer) < sum(hand):
                print("The dealer will hit now")
            card = deck.pop()
            if card == 11: card = hash["J"]
            if card == 12: card = hash["Q"]
            if card == 13: card = hash["K"]
            if card == 14: card = hash["A"]
            dealer.append(card)
            print(f"The dealer draws {card}")
            print(f"The dealer's total is now {sum(dealer)}")
            if sum(dealer) >= sum(hand) and sum(dealer) < 22:
                print("The dealer won")
                blah = playagain()
                if not blah:
                    return
                # lose = lose +1
            if sum(dealer) > 21:
                print ("The dealer has busted, you win!")
                playagain()
                # win = win +1





# dealplayer(deck)
# dealhouse(deck)
# hit(deck)

# print(f"You have won {win} times and lost {lose} times.")
def playagain():
    playagain = input("Would like To play again? \n Yes \n No \n")
    hand = []
    dealer = []
    if playagain == "Yes" or playagain == "yes":
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        hash = {
            "J": 10,
            "Q": 10,
            "K": 10,
            "A": 1
        }
        dealplayer(deck, hand)
        dealhouse(deck, dealer)
        hit(deck, hand, dealer)
        return True
    if playagain == "No" or playagain == "no":
        print("Thanks for playing!")
        return False
# else:
#     print("Thanks for playing!")

# playagain()
dealplayer(deck, hand)
dealhouse(deck, dealer)
hit(deck, hand, dealer)
