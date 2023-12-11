from helpers import readFile, getNums

def main():
    lines = readFile("day11.txt")
    
    part1 = 0
    part2 = 0
    
    height = len(lines)
    width = len(lines[0])
    
    empty_rows = set(range(height))
    empty_cols = set(range(width))
    
    galaxies = []
    
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == "#":
                if r in empty_rows:
                    empty_rows.remove(r)
                if c in empty_cols:
                    empty_cols.remove(c)
                galaxies.append((r, c))
    
    factor1 = 2
    factor2 = 1000000
    
    for i1, g1 in enumerate(galaxies[:-1]):
        for i2 in range(i1 + 1, len(galaxies)):
            g2 = galaxies[i2]
            
            high_row = max(g2[0], g1[0])
            low_row = min(g2[0], g1[0])
            high_col = max(g2[1], g1[1])
            low_col = min(g2[1], g1[1])

            row_expands = len([x for x in empty_rows if x < high_row and x > low_row])
            col_expands = len([x for x in empty_cols if x < high_col and x > low_col])

            part1 += abs(g2[1] - g1[1]) + abs(g2[0] - g1[0]) + (row_expands + col_expands) * (factor1 - 1)
            part2 += abs(g2[1] - g1[1]) + abs(g2[0] - g1[0]) + (row_expands + col_expands) * (factor2 - 1)
        
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
