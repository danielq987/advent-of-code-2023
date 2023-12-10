import re

def readFile(filename):
    lines = []
    with open(f"../input/{filename}") as f:
        lines = [line.strip() for line in f]
    return lines

def getNums(line, negative=False):
    reString = "[0-9-]+" if negative else "\d+"
    return [int(num) for num in re.findall(reString, line)]