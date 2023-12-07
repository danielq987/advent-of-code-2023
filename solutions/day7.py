from helpers import readFile, getNums

cards1 = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
cards2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

N = len(cards1)

def parseHand(hand, useJokers=False):
    cardList = cards2 if useJokers else cards1
    
    return [cardList.index(card) for card in hand]
    
def getHandValue(hand, useJokers=False):
    # Get card frequencies
    freq = {card: hand.count(card) for card in set(hand)}
    jokerCount = 0
    if useJokers:
        jokerCount = freq.get(0, 0)
        # Set number of jokers to 0
        freq[0] = 0
    # Sort frequencies by size
    freqs = list(reversed(sorted(freq.values()))) + [0]

    # Add joker to most frequent non-joker card
    freqs[0] += jokerCount

    # Highest type score is 5 of kind (freqs[0] = 5)
    typeScore = freqs[0] * 3 + freqs[1]
        
    tieScore = 0
    for ind, card in enumerate(hand):
        tieScore += N ** (4 - ind) * card
        
    return typeScore * (N ** 5) + tieScore

def main():
    lines = readFile("day7.txt")
    
    l_raw = [line.split(" ") for line in lines]
    
    for useJokers in [False, True]:
        l = [(parseHand(hand, useJokers), int(bid), hand) for hand, bid in l_raw]
        l = sorted(l, key=lambda x: getHandValue(x[0], useJokers))
        
        winnings = 0

        for ind, hand in enumerate(l):
            rank = ind + 1
            winnings += rank * hand[1]
            
        print(winnings)
        
if __name__ == "__main__":
    main()
