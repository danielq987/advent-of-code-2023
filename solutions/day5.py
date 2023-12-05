from helpers import readFile

# Part one - simple mapping. Applies a list of tuples (maps) onto a singular value, returns the result.
def applyMap(num, maps):
    for dest, src, length in maps:
        if num in range(src, src + length):
            return dest + (num - src)
    # number was not encompassed in the map, no effect
    return num

def rangeIntersection(range1, range2):
    return (max(range1[0], range2[0]), min(range1[1], range2[1]))

# Part two - range mapping. Applies a list of tuples (maps) onto a whole range. Returns a list of ranges.
def applyMapRange(num_start, num_end, maps):
    mapped_ranges = []

    # List of range of numbers to remain unmapped
    remaining_seeds = [(num_start, num_end)]
    for dest, src, length in maps:
        # Get the intersection between map source range and number range
        overlap = rangeIntersection((num_start, num_end), (src, src + length))

        # Non-zero intersection (i.e. at least one value is mapped using that line)
        if overlap[0] < overlap[1]:
            mapped_ranges.append((dest + overlap[0] - src, dest + overlap[1] - src))

            # Keep track of which ranges remain unmapped - remove all the mapped numbers from remaining_numbers
            new_remaining = []

            # Iterate over each remaining range and subtract out the just-mapped elements from the range
            for r_start, r_end in remaining_seeds:
                # Get intersection between mapped numbers and remaining range - represents the just mapped region.
                r_range = rangeIntersection((r_start, r_end), overlap)

                # No intersection - no effect, no numbers need to be removed from this specific range
                if r_range[0] > r_range[1] or r_range[1] < r_range[0]:
                    continue

                # Numbers left of the mapped region still unmapped.
                if r_range[0] > r_start:
                    new_remaining.append((r_start, r_range[0]))
                # Number right of the mapped region still unmapped
                if r_range[1] < r_end:
                    new_remaining.append((r_range[1], r_end))
            
            # Update the remaining array
            remaining_seeds = new_remaining
    
    # Return the unmapped remaining numbers as is, plus the updated mapped ranges
    return remaining_seeds + mapped_ranges

def main():
    lines = readFile("day5.txt")
    
    seeds, _, *lines = lines

    seeds1 = [int(seed) for seed in seeds.split()[1:]]
    seeds2 = []
    for i in range(0, len(seeds1), 2):
        seeds2.append((seeds1[i], seeds1[i] + seeds1[i + 1]))
    mapsList = []

    i = 0

    # Text processing
    while i < len(lines) - 1:
        i += 1
        m = []
        # Process the maps
        while True:
            l = lines[i].strip().split()
            # Make sure the line is a proper map - otherwise there are no more lines
            if len(l) != 3:
                break
            m.append([int(n) for n in l])
            i += 1
        mapsList.append(m)
        i += 1

    # Loop over types of maps
    for m in mapsList:
        for i, val in enumerate(seeds1.copy()):
            seeds1[i] = applyMap(val, m)
        new_seeds= []
        for i, ranges in enumerate(seeds2.copy()):
            new_ranges = applyMapRange(ranges[0], ranges[1], m)
            new_seeds = new_seeds + new_ranges
        seeds2 = new_seeds

    # Part 1    
    print(min(seeds1))
    # Part 2
    print(min([seed[0] for seed in seeds2]))

if __name__ == "__main__":
    main()
