from helpers import readFile
from collections import defaultdict
import re

lookup = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def convert_to_number(num_str):
    try:
        return int(num_str)
    except:
        return lookup[num_str]

def main():
    lines = readFile("day1.txt")

    part1 = 0
    part2 = 0

    # Build the regex
    number_words = '|'.join(list(lookup.keys()))
    nongreedy = f"^.*?(\d|{number_words})"
    greedy = f"^.*(\d|{number_words})"

    for line in lines:
        digits = re.findall('\d', line)
        part1 = int(convert_to_number(digits[0])*10+convert_to_number(digits[1]))

        num1 = re.findall(nongreedy, line) # Non-greedy gets the first match
        num2 = re.findall(greedy, line) # Greedy gets the last match
        part2 += int(convert_to_number(num1[0])*10+convert_to_number(num2[0]))

    print(part1)
    print(part2)
    
if __name__ == "__main__":
    main()
