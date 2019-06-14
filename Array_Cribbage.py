from enum import Enum
import math

class Suit:
    Club = "club"
    Diamond = "diamond"
    Heart = "hearts"
    Spade = "spade"

class Card:
    def __init__(self, Suit, rank):
        self.suit = Suit
        self.rank = rank

class Cribbage:
    def __init__(self, cards):
        if len(cards) != 5:
            raise StandardError("Exactly 5 cards need to be passed for the cribbage points calculation!")
        self.cards = cards
        self.total = 0

    
    def Flush(self):
        suit = self.cards[0].suit
        for i in range(1, 5):
            if self.cards[i].suit != suit:
                return "No flush. Your total points are: " + str(self.total)
        self.total += 5
        return "Flush! Your total points are now: " + str(self.total)

    
    def Pairs(self):
        rankCount = {}
        for card in self.cards:
            if card.rank not in rankCount:
                rankCount[card.rank] = 1
            else:
                rankCount[card.rank] += 1

        pairsExist = False
        pairsCount = 0
        for count in rankCount.values():
            if count > 1:
                pairsExist = True
                pairsCount += math.factorial(count) / (math.factorial(2) * math.factorial(count - 2))
                self.total += math.factorial(count) / (math.factorial(2) * math.factorial(count - 2)) * 2
        
        if pairsExist:
            return "Pairs found!\nTotal pairs found: " + str(pairsCount) + ".\nYour total points are now: " + str(self.total)
        else:
            return "No pairs found. Your total points are: " + str(self.total)


    def Fifteens(self):
        sortedRanks = sorted([c.rank for c in self.cards])
        for i in range(0, len(sortedRanks)):
            for j in range(i+1, len(sortedRanks)):
                self.findTarget([sortedRanks[i]] + sortedRanks[j:len(sortedRanks)], 0, 15)
        return "Fifteens checked. Your total points now are: " + str(self.total)

    def findTarget(self, arr, currentTotal, target):
        if target not in arr and len(arr) > 0 and target > arr[0]:
            currentTotal += arr[0]
            target = 15 - currentTotal
            self.findTarget(arr[1:len(arr)], currentTotal, target)
        elif target in arr:
            self.total += 2
    

if __name__ == '__main__':
    c1 = Card(Suit.Heart, 1)
    c2 = Card(Suit.Heart, 2)
    c3 = Card(Suit.Heart, 2)
    c4 = Card(Suit.Heart, 3)
    c5 = Card(Suit.Spade, 10)

    cribbage = Cribbage([c1, c2, c3, c4, c5])
    # print cribbage.Flush()
    # print cribbage.Pairs()
    print cribbage.Fifteens()