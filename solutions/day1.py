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
    
    # Do some data processing here
    lines = [line for line in lines]

    s = 0

    number_words = '|'.join(list(lookup.keys()))

    nongreedy = f"^.*?(\d|{number_words})"
    greedy = f"^.*(\d|{number_words})"
    for line in lines:
        num1 = re.findall(nongreedy, line)
        num2 = re.findall(greedy, line)
        value = int(convert_to_number(num1[0])*10+convert_to_number(num2[0]))
        s += value

    print(s) 
    
    # print(re.findall(reString, "oneight", overlapped=True))
    
if __name__ == "__main__":
    main()
