from helpers import readFile, getNums

def main():
    raw = readFile("day13.txt")
    
    raw = '\n'.join(raw)

    patterns = raw.split('\n\n')

    def find_mirror_row(lines, errors):
        # Try mirror at each row
        for ind, _ in enumerate(lines[0:-1]):
            l = ind
            r = ind + 1

            err = errors

            # Validate the reflections are correct
            while l >= 0 and r < len(lines) and err >= 0:
                if lines[l] != lines[r]:
                    # If reflections are incorrect, count the number of discrepancies
                    e = sum([0 if cl == cr else 1 for cl, cr in zip(lines[l], lines[r])])
                    err -= e
                l -= 1
                r += 1

            if err == 0:
                print(ind + 1)
                return ind + 1
        return -1
    
    ans = [0, 0];
    for ind, num_error in enumerate([0, 1]):
        for pattern in patterns:
            p_lines = pattern.split('\n')

            # Assume mirror is horizontal
            mirror_pos = find_mirror_row(p_lines, num_error)
            inv_lines = [''.join(line) for line in zip(*p_lines)]

            if mirror_pos == -1:
                # No mirror found horizontally, try vertical mirror
                mirror_pos = find_mirror_row(inv_lines, num_error)
                ans[ind] += mirror_pos
            else:
                ans[ind] += mirror_pos * 100

    print(f"Part 1: {ans[0]}")
    print(f"Part 2: {ans[1]}")

if __name__ == "__main__":
    main()
