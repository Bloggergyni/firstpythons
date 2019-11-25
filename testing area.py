import random
import turtle
import time

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
random.shuffle(deck)
wallet = 100
pot = 0
dealer = []
hand = []
hash = {
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 1
}


def endgame():
    turtle.bye()


def wipescreen(wallet):
    pot = 0
    dealer = []
    hand = []

    turtle.reset()
    turtle.speed(speed=0)
    turtle.ht()
    turtle.penup()
    turtle.goto(330, 350)
    turtle.write(f"Your wallet: ${wallet}", font=(12))
    turtle.goto(-450, 200)
    turtle.write("Table rules: lose your wallet lose your life!")
    turtle.goto(-450, 375)
    turtle.write("Welcome to Gabe's 21 where the decks are stacked and ready to be racked.", font=(12))
    turtle.home

    return pot, dealer, hand


def initialbet(wallet):
    pot = turtle.numinput("Bet", "How much do you want to bet? The minimum for this table is $1!\n", minval=1,
                          maxval=wallet)
    wallet = wallet - pot
    turtle.goto(330, 330)
    turtle.color("red")
    turtle.write(f"Your wallet: ${wallet}", font=(12))
    turtle.color("green")
    turtle.goto(150, 250)
    turtle.write(f"You have bet ${pot}, good luck!", font=(12))
    turtle.color("black")

    return pot, wallet


def dealhands(deck, hand, dealer):
    for i in range(2):
        card = deck.pop()
        if card == 11: card = hash["J"]
        if card == 12: card = hash["Q"]
        if card == 13: card = hash["K"]
        if card == 14: card = hash["A"]
        hand.append(card)
    for i in range(2):
        card = deck.pop()
        if card == 11: card = hash["J"]
        if card == 12: card = hash["Q"]
        if card == 13: card = hash["K"]
        if card == 14: card = hash["A"]
        dealer.append(card)
    turtle.goto(-450, 150)
    turtle.write(f"You have received a {hand[0]} and a {hand[1]} totaling {sum(hand)}.", font=(12))
    turtle.goto(0, 150)
    turtle.write(f"The dealer shows a {dealer[0]} and a smile.", font=(12))

    return deck, hand, dealer


# def deckhitinit():
#     deckhit(deck,hand)
#     return(deck,hand)

def deckhit(deck, hand):
    card = deck.pop()
    if card == 11: card = hash["J"]
    if card == 12: card = hash["Q"]
    if card == 13: card = hash["K"]
    if card == 14: card = hash["A"]
    hand.append(card)
    turtle.goto(-450, 150 - (20 * len(hand) - 40))
    if sum(hand) > 21: turtle.color("red")
    turtle.write(f"You add a {card} to your hand which now totals {sum(hand)}.", font=(12))
    turtle.color("black")
    if sum(hand) > 21:
        turtle.goto(-250, -250)
        turtle.color("red")
        turtle.write(f"Your hand totals {sum(hand)}. YOU BUSTED BRO!", font=("Comic Sans MS", 24))
        return deck, hand
    return deck, hand


# def winnerinit():
#     winnercheck(hand,dealer,deck)


def winnercheck(hand, dealer, deck):
    if sum(hand) > 21:
        return dealer, deck
    turtle.goto(0, 130)
    turtle.write(f"The dealer reveals they had a {dealer[0]} and a {dealer[1]} totaling {sum(dealer)}.", font=(12))
    while sum(hand) > sum(dealer) and sum(hand) < 22:
        dealerhit(deck, dealer)
    return dealer, deck


def dealerhit(deck, dealer):
    time.sleep(1)
    card = deck.pop()
    if card == 11: card = hash["J"]
    if card == 12: card = hash["Q"]
    if card == 13: card = hash["K"]
    if card == 14: card = hash["A"]
    dealer.append(card)
    turtle.goto(0, 150 - (20 * len(dealer) - 20))
    turtle.write(f"The dealer draws a {card} he now shows {sum(dealer)}.", font=(12))

    return deck, dealer


turtle.onkey(endgame, "Escape")
# turtle.onkey(deckhitinit,"Down")
# turtle.onkey(winnerinit,"Up")
# turtle.onkey(gamecycle,"Right")


while wallet > 0:
    usersays = 1
    pot, dealer, hand = wipescreen(wallet)
    print(f"wipescreen wallet: {wallet} and pot: {[pot]}")
    pot = initialbet(wallet)
    pot = pot[0]
    print(f"initial bet wallet: {wallet} and pot: {[pot]}")

    deck, hand, dealer = dealhands(deck, hand, dealer)

    while usersays == 1:
        if sum(hand) > 21: break
        usersays = turtle.numinput("Take a card?", "1: Yes, 2: No")
        if usersays != 1:
            break
        deck, hand = deckhit(deck, hand)
    dealer, deck = winnercheck(hand, dealer, deck)

    if sum(dealer) >= sum(hand) and sum(dealer) < 22:
        turtle.speed(1)
        turtle.write(f"YOU LOST BRO!", font=("Comic Sans MS", 36))
        turtle.speed(0)
        print(f"wallet: {wallet} and pot: {[pot]}")
        time.sleep(2)
        wallet = wallet - pot
        continue

    if sum(hand) > 21:
        turtle.speed(1)
        turtle.write(f"YOU LOST BRO!", font=("Comic Sans MS", 36))
        turtle.speed(0)
        print(f"wallet: {wallet} and pot: {[pot]}")
        time.sleep(2)
        wallet = wallet - pot
        continue

    if sum(dealer) > 21 and sum(hand) < 22:
        turtle.speed(1)
        turtle.write(f"YOU WON BRO!", font=("Comic Sans MS", 36))
        turtle.speed(0)
        print(f"wallet: {wallet} and pot: {[pot]}")
        time.sleep(2)
        wallet = wallet + pot
        continue

if wallet < 1:
    wipescreen(wallet)
    turtle.goto(0, 0)
    turtle.write(f"Your legs get broken... \npress escape to die", font=("Comic Sans MS", 36))

turtle.listen()

turtle.mainloop()


