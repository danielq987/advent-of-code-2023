from helpers import readFile, getNums

def main():
    lines = readFile("day15.txt")[0]
    
    part1 = 0
    part2 = 0

    def hash_(s):
        cv = 0
        for char in s:
            cv += ord(char)
            cv *= 17
            cv = cv % 256
        return cv
    
    boxes = [({}, []) for i in range(256)]

    for s in lines.split(","):
        part1 += hash_(s)
        label = ""
        foc = 0
        instr = "remove"
        if "=" in s:
            label, num = s.split("=")
            foc = int(num)
            instr = "add"
        else:
            label = s[:-1]

        focLookup, boxQ = boxes[hash_(label)]

        if instr == "remove":
            if label in focLookup:
                boxQ.remove(label)
                focLookup.pop(label)
        else:
            if label in focLookup:
                focLookup[label] = foc
            else:
                boxQ.append(label)
                focLookup[label] = foc

    for i, box in enumerate(boxes):
        focLookup, boxQ = box
        for j, label in enumerate(boxQ):
            part2 += (i + 1) * (j + 1) * focLookup[label]
                

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
