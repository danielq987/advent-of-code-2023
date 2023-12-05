from helpers import readFile

def main():
    lines = readFile("day4.txt")
    
    # Do some data processing here
    
    part1 = 0
    part2 = 0
    
    lookup = {}

    for card, line in enumerate(lines):
        a = line.split("|")
        winning = [int(num) for num in a[0].strip().split(":")[1].strip().split()]
        scratch = [int(num) for num in a[1].strip().split()]

        intersect = len(set(winning) & set(scratch))
        
        if intersect:
            part1 += 2 ** (intersect - 1)

        for i in range(intersect):
            lookup[card + i + 1] = lookup.get(card + i + 1, 1) + lookup.get(card, 1)
        part2 += lookup.get(card, 1)
        
    print(part1)
    print(part2)
    
if __name__ == "__main__":
    main()
