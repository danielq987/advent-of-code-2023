from helpers import readFile, getNums

def main():
    lines = readFile("day16.txt")
    
    part1 = 0
    part2 = 0

    height = len(lines)
    width = len(lines[0])

    # 0123, up, right, down, left
    def processDir(r, c, dir):
        if dir == 2:
            r += 1
        elif dir == 0:
            r -= 1
        elif dir == 1:
            c += 1
        elif dir == 3:
            c -= 1
            
        if r < 0 or c < 0 or r >= height or c >= width:
            return []
        
        isHorizontal = dir % 2 == 1
        
        char = lines[r][c]
        beams = []

        if char == "." or (
            char == "-" and isHorizontal) or (
            char == "|" and not isHorizontal
            ):
            beams.append((r, c, dir))
        elif char == "\\":
            l = {0:3, 1:2, 2:1, 3:0}
            beams.append((r, c, l[dir]))
        elif char == "/":
            l = {0:1, 1:0, 2:3, 3:2}
            beams.append((r, c, l[dir]))
        elif char == "-":
            beams.append((r, c, 1))
            beams.append((r, c, 3))
        else:
            beams.append((r, c, 0))
            beams.append((r, c, 2))
        
        return beams
        
    for r in range(height):
        for ind, start in enumerate([(r, -1, 1), (r, width, 3), (-1, r, 2), (height, r, 0)]):
            qbeams = [start]
            lookup = {}
            while qbeams:
                br, bc, dir = qbeams.pop(0)
                if (br, bc) in lookup and dir in lookup[(br, bc)]:
                    continue
                lookup[(br, bc)] = lookup.get((br, bc), []) + [dir]
                newBeams = processDir(br, bc, dir)
                qbeams = qbeams + newBeams
        
            if r == 0 and ind == 0:
                part1 = max(len(lookup) - 1, part1)
            else:
                part2 = max(len(lookup) - 1, part2)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
