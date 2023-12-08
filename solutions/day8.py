from helpers import readFile, getNums
from re import findall
from math import lcm

lookup = {}

def main():
    lines = readFile("day8.txt")

    dirs = lines[0]
    l_dirs = len(dirs)
    i_dirs = 0

    def goNext(state, direction):
        d = 0 if direction == "L" else 1
        try:
            new_state = lookup[state][d]
            return new_state
        except:
            return ""
        
    state = "AAA"
    
    part1 = 0
    part2 = 0
    
    for line in lines[2:]:
        txts = findall("\w+", line)
        lookup[txts[0]] = (txts[1], txts[2])
    
    states2 = [k for k in lookup.keys() if k[2] == "A"]
    endTimes = [[0] for k in lookup.keys() if k[2] == "A"]
        
    while state != "ZZZ":
        state = goNext(state, dirs[i_dirs])
        if not state:
            break

        i_dirs += 1
        if i_dirs >= l_dirs:
            i_dirs = 0

        part1 += 1
        
    i_dirs = 0
    for counter in range(100000):
        for i, s in enumerate(states2):
            new_s = goNext(s, dirs[i_dirs])
            if new_s[2] == "Z":
                endTimes[i].append(counter+1)
            states2[i] = new_s 
        i_dirs += 1
        if i_dirs >= l_dirs:
            i_dirs = 0
    
    part2 = lcm(*[cycles[1] for cycles in endTimes])

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
