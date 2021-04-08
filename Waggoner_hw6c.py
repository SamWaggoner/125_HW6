# File: hw6c.py
# Author: Sam Waggoner
# Date: 10/27/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# Create various card-related functions.
# Collaboration:
# I did not discuss this assignment with anyone outside of the course staff.
# I talked briefly with Zac.

import random

# no parameters, returns list
def emptydeck():
    deck = []
    return deck

# no parameters, returns list
def makedeck():
    deck = []
    for suit in range(1,5):
        for cardnum in range(1,14):
            list1 = [suit,cardnum]
            deck.append(list1)
            list1 = []
    return deck

# parameter: list, returns list
def shuffle(deck):
    shuffled_deck = []
    for i in range(len(deck)):
        card = deck.pop(random.randint(0,len(deck)-1))
        shuffled_deck.append(card)
    return shuffled_deck

# parameter: list,number, returns list
def topcards(deck,number):
    if deck != emptydeck():
        cardlist = []
        for i in range(number):
            card = deck.pop(i)
            cardlist.append(card)
        return cardlist

# parameter: list,number, returns list
def discard(card,number):
    discardpile = []
    for i in range(number):
        discardpile.insert(0,card[i])
    return discardpile

# parameter: list, prints list
def printoff(deck):
    for i in range(len(deck)):
        if deck[i][1] == 1:
            a = "ace"
        if deck[i][1] == 2:
            a = "two"
        if deck[i][1] == 3:
            a = "three"
        if deck[i][1] == 4:
            a = "four"
        if deck[i][1] == 5:
            a = "five"
        if deck[i][1] == 6:
            a = "six"
        if deck[i][1] == 7:
            a = "seven"
        if deck[i][1] == 8:
            a = "eight"
        if deck[i][1] == 9:
            a = "nine"
        if deck[i][1] == 10:
            a = "ten"
        if deck[i][1] == 11:
            a = "jack"
        if deck[i][1] == 12:
            a = "queen"
        if deck[i][1] == 13:
            a = "king"
            # suit
        if deck[i][0] == 1:
            b = "clubs"
        if deck[i][0] == 2:
            b = "diamonds"
        if deck[i][0] == 3:
            b = "hearts"
        if deck[i][0] == 4:
            b = "spades"
        print (a+" of "+b)

def main():
    
    print("Generate a new deck and print it.")
    print("---------------------------------------------------------------------")
    printoff(makedeck())
    deck = makedeck()

    print()
    print()

    print("Shuffle a deck and print it.")
    print("---------------------------------------------------------------------")
    deck = shuffle(deck)
    printoff(deck)

    print()
    print()
    
    print("Draw five cards off a deck, printing each.")
    print("---------------------------------------------------------------------")
    printoff(topcards(deck,5))
    
    print()
    print()

    print("Shuffle and print again.")
    print("---------------------------------------------------------------------")
    printoff(shuffle(deck))

    print()
    print()

    print("Add ten cards to a previously empty discard deck, printing the result.")
    print("---------------------------------------------------------------------")
    printoff(discard(shuffle(makedeck()),10))

main()