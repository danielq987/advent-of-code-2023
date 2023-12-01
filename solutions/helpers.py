def readFile(filename):
    lines = []
    with open(f"../input/{filename}") as f:
        lines = [line.strip() for line in f]
    return lines
