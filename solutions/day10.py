from helpers import readFile
from sys import setrecursionlimit

def main():
    setrecursionlimit(100000)
    lines = readFile("day10.txt")
    
    part1 = 0
    part2 = 0
    
    row_start = 0
    col_start = 0
    
    height = len(lines)
    width = len(lines[0])
    
    # Enter these in manually lol
    start_char = "7"
    start_approach_dir = "L"
    
    for ind, line in enumerate(lines):
        try:
            col_start = line.index("S")
            row_start = ind
            lines[ind] = line[0:col_start] + start_char + line[col_start + 1:]
            break
        except Exception as e:
            pass
    
    # 1 is right, -1 is left, 10 is down, -10 is up
    d_lookup = {
        "-": ("L", "R"),
        "|": ("D", "U"),
        "L": ("R", "U"),
        "F": ("D", "R"),
        "7": ("D", "L"),
        "J": ("L", "U"),
        ".": ()
    }

    inv = {
        "L": "R",
        "R": "L",
        "U": "D",
        "D": "U",
    }
    
    tracking = {}
    
    def followPipe(pos, prev, steps, firstTime=False):
        # base case
        if pos == (row_start, col_start) and not firstTime:
            return steps

        row, col = pos
        dirs = d_lookup[lines[row][col]]
        
        # find the direction to continue in (that we did not originate from)
        next_dir = dirs[0] if prev == dirs[1] else dirs[1]
        
        row, col = applyDir(pos, next_dir)
        tracking[pos] = next_dir
        
        # continue following the pipe
        return followPipe((row, col), inv[next_dir], steps + 1)

    def applyDir(pos, dir):
        row, col = pos
        if dir == "U":
            row -= 1
        elif dir == "D":
            row += 1
        elif dir == "L":
            col -= 1
        elif dir == "R":
            col += 1
        return row, col
    
    part1 = followPipe((row_start, col_start), start_approach_dir, 0, True) / 2
    
    in_tiles = 0
    
    for r, line in enumerate(lines):
        c = 0
        while c < width:
            num_tiles = 0
            
            # Count tiles until the next pipe tile
            while c < width and (r, c) not in tracking:
                num_tiles += 1
                c += 1
            
            # If no non-pipe tiles or reached the end of the row, move on
            if num_tiles == 0 or c == width:
                c += 1 
                continue
        
            char = line[c]
            dir = tracking[(r, c)]
            
            # This condition assumes a counterclockwise loop
            if (((char == "|" or char == "L") and dir == "U")
                or (char == "F" and dir == "R")):
                in_tiles += num_tiles
    
    part2 = in_tiles
    
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
