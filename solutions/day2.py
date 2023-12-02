from helpers import readFile

def main():
    lines = readFile("day2.txt")
    
    lines = [line.split(":")[1] for line in lines]
    
    color_max = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    
    part1 = 0
    part2 = 0
    
    for index, line in enumerate(lines):
        games = line.split(";")
        is_invalid = False
        rgb = {}
        for game in games:
            colors = game.strip().split(",")
            for color in colors:
                num, color_name = color.strip().split(" ")
                num = int(num)
                rgb[color_name] = max(num, rgb.get(color_name, 0))
                if num > color_max[color_name]:
                    is_invalid = True

        if not is_invalid:
            part1 += 1 + index
        
        power = rgb.get("red", 0) * rgb.get("green", 0) * rgb.get("blue", 0)
        part2 += power

    print(part1)
    print(part2)

if __name__ == "__main__":
    main()
