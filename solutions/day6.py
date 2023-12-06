from helpers import readFile, getNums
import re
from math import sqrt, ceil, floor

def main():
    lines = readFile("day6.txt")
    
    part1 = 1
    part2 = 0

    times = getNums(lines[0])
    dists = getNums(lines[1])

    t2 = int(''.join([str(time) for time in times]))
    d2 = int(''.join([str(dist) for dist in dists]))

    def solve(time, dist):
        sol2 = (-time - sqrt(time ** 2 - (4 * -1 * -dist)))/(-2)
        sol1 = (-time + sqrt(time ** 2 - (4 * -1 * -dist)))/(-2)
        return floor(sol2 - 0.0001) - ceil(sol1 + 0.0001) + 1


    for time, dist in zip(times, dists):
        part1 *= solve(time, dist)
    
    part2 = solve(t2, d2)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
