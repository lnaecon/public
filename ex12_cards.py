from cards import Card
from random import random, randrange
from graphics import *
from tkinter.filedialog import askopenfilename


def cat(list):
    # break list of card objects
    rank_list = []
    suit_list = []
    for i in list:
        rank_list.append(i[0])
        suit_list.append(i[1])

    rank_list.sort()
    suit_list.sort()
    print(rank_list)

    def royal_flush(r, s):
        r_check = False
        if (r[0] == 1) and (r[1] == 10) and (r[4] == 13):
            r_check = True
        if r_check and flush(s):
            return True
        else:
            return False

    def straight_flush(r, s):
        if straight(r) and flush(s):
            return True
        else:
            return False

    def four_kind(r):
        if r[0] == r[3] or r[1] == r[4]:
            return True
        else:
            return False

    def full_house(r):
        if (r[0] == r[2] and r[3] == r[4]) or (r[0] == r[1] and r[2] == r[4]):
            return True
        else:
            return False

    def flush(s):
        if s[0] + s[1] + s[2] + s[3] + s[4] == s[0] * len(s):
            return True
        else:
            return False

    def straight(r):
        n = 0
        straight = True
        while n < len(r) - 1:
            if r[n] + 1 != r[n + 1]:
                straight = False
            n = n + 1
        return straight

    def three_kind(r):
        # only used after full house or four of a kind
        if (r[0] == r[2]) or (r[2] == r[4]) or (r[1] == r[3]):
            return True
        else:
            return False

    def two_pair(r):
        # only used after not straight or full house
        n = 0
        count = 0
        while n < len(r) - 1:
            if r[n + 1] == r[n]:
                count = count + 1
            n = n + 1
        if count == 2:
            return True
        else:
            return False

    def pair(r):
        # only used after not straight or full house or two pair
        n = 0
        count = 0
        while n < len(r) - 1:
            if r[n + 1] == r[n]:
                count = count + 1
            n = n + 1
        if count == 1:
            return True
        else:
            return False

    if royal_flush(rank_list, suit_list):
        return "Royal Flush"
    elif straight_flush(rank_list, suit_list):
        return "Straight Flush"
    elif four_kind(rank_list):
        return "Four of a Kind"
    elif full_house(rank_list):
        return "Full House"
    elif flush(suit_list):
        return "Flush"
    elif straight(rank_list):
        return "Straight"
    elif three_kind(rank_list):
        return "Three of a Kind"
    elif two_pair(rank_list):
        return "Two Pair"
    elif pair(rank_list):
        return "Pair"
    else:
        return str(max(rank_list)) + " high"

def main():
    '''
    input_file = askopenfilename()
    infile = open(input_file, "r")
    card_list = []
    for line in infile:
        # assume rank, then suit separated by " "
        r, s = line.split()
        card_list.append([int(r), s])

    # first sort by rank
    card_list.sort()
    '''
    # generate random card list
    card_list = []
    for i in range(6):
        rank = randrange(1, 14)
        suit_list = ["d", "s", "h", "c"]
        suit = suit_list[int(random() * 4)]
        card_list.append([rank, suit])

    # create windows
    win = GraphWin("Cards", 800, 600)
    win.setBackground("tan")

    # create list of Card objects
    count = 0
    for i in card_list:
        rank, suit = i[0], i[1]
        one_card = Card(rank, suit)
        one_card.draw(win, Point(120 * (count + 1), 300))
        count = count + 1

    result = Text(Point(400, 100), cat(card_list))
    result.setFill("red")
    result.setSize(25)
    result.draw(win)

    '''
    # then sort Card objects by suit
    def use_suit(Card):
        return Card.getSuit()
    print_list.sort(key=use_suit)

    for i in print_list:
        print(i)
    '''

    win.getMouse()
    win.close()

main()


