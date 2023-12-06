import re

def readFile(filename):
    lines = []
    with open(f"../input/{filename}") as f:
        lines = [line.strip() for line in f]
    return lines

def getNums(line):
    return [int(num) for num in re.findall("\d+", line)]