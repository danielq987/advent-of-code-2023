from helpers import readFile

lookup = {}

def checkSymbol(row, col_begin, col_end, lines, num):
    isAdjacent = False
    for r in range(max(0, row - 1), min(len(lines) - 1, row + 2)):
        for c in range(max(0, col_begin - 1), min(len(lines[0]) - 1, col_end + 1)):
            if not lines[r][c].isdigit() and lines[r][c] != ".":
                # For part 2: store all numbers beside each asterisk in a lookup table
                if lines[r][c] == "*":
                    lookup[(r, c)] = lookup.get((r, c), []) + [num]
                isAdjacent = True
    return isAdjacent

def main():
    lines = readFile("day3.txt")
    
    # Do some data processing here
    lines = [line for line in lines]

    part1 = 0
    part2 = 0

    for row, line in enumerate(lines):
        col = 0
        # Loop through the line
        while col < len(line):
            chr = line[col]
            if chr.isdigit():
                num_start = col
                col += 1
                while col < len(line) and line[col].isdigit():
                    col += 1
                num = int(line[num_start:col])
                if checkSymbol(row, num_start, col, lines, num):
                    part1 += num
            col += 1
                
                
    for nums in lookup.values():
        if len(nums) == 2:
            part2 += nums[0]*nums[1]
    
    print(part1)
    print(part2)

if __name__ == "__main__":
    main()
