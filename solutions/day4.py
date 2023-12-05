from helpers import readFile
from collections import defaultdict

def main():
    lines = readFile("day4.txt")
    
    part1 = 0
    part2 = 0
    
    lookup = defaultdict(lambda: 1)

    for card, line in enumerate(lines):
        winning, scratch = line.split("|")
        winning = [int(num) for num in winning.strip().split(":")[1].strip().split()]
        scratch = [int(num) for num in scratch.strip().split()]

        intersect = len(set(winning) & set(scratch))
        
        if intersect:
            part1 += 2 ** (intersect - 1)

        for i in range(intersect):
            lookup[card + i + 1] = lookup[card + i + 1]+ lookup[card]
        part2 += lookup[card]
        
    print(part1)
    print(part2)
    
if __name__ == "__main__":
    main()
