from helpers import readFile, getNums

def main():
    
    def helper(l, is_backwards):
        if not any(l):
            return 0
        diff = [l[ind] - l[ind - 1] for ind in range(1, len(l))]
        
        index = 0 if is_backwards else -1
        sgn = -1 if is_backwards else 1
        
        return l[index] + (helper(diff, is_backwards)) * sgn
        
    lines = readFile("day9.txt")
    
    part1 = 0 
    part2 = 0 

    lines = [getNums(line, True) for line in lines]
    
    for line in lines:
        part1 += helper(line, is_backwards=False)
        part2 += helper(line, is_backwards=True)
        
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
