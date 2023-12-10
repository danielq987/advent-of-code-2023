from helpers import readFile, getNums

def main():
    
    def helper(l, is_backwards):
        ret = []
        is_zero = True
        for ind, num in enumerate(l[1:]):
            a = l[ind + 1] - l[ind]
            ret.append(a) 
            if a != 0:
                is_zero = False
        
        if is_backwards:
            if is_zero:
                return l[0]
            return l[0] - helper(ret, is_backwards)
        else:
            if is_zero:
                return l[-1]
            return l[-1] + helper(ret, is_backwards)

        
    lines = readFile("day9.txt")
    
    part1 = 0 
    part2 = 0 

    lines = [getNums(line, True) for line in lines]
    
    for line in lines:
        part1 += helper(line, False)
        part2 += helper(line, True)
        
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
