from helpers import readFile, getNums

def main():
    lines = readFile("day14.txt")
    
    part1 = 0
    part2 = 0


    lines = [[char for char in line] for line in lines]

    boardStates = {}

    def rotateBoard(board):
        return [list(line) for line in zip(*board[::-1])]

    def shiftUp(board):
        l = len(board)
        for row, line in enumerate(board):
            for col, char in enumerate(line):
                i = row
                j = col

                if char == "O":
                    while i > 0 and board[i - 1][j] == ".":
                        i -= 1

                    if i != row:
                        board[row][col] = "."
                        board[i][j] = "O"
        return board
    
    def countWeights(board):
        s = 0
        l = len(board)
        for row, line in enumerate(board):
            for col, char in enumerate(line):
                if char == "O":
                    s += l - row 

        return s

    # Notice that the board repeats in periods of 35
    # 90 === 1000000000 (mod 35)
    # Any other smaller congruent number has not settled into the cycle yet (by observation)
    for i in range(90):
        for j in range(4):
            lines = shiftUp(lines)
            if i == 0 and j == 0:
                part1 = countWeights(lines)
            lines = rotateBoard(lines)
        s = '\n'.join([''.join(line) for line in lines])
        
        if s in boardStates:
            boardStates[s].append(i)
        else:
            boardStates[s] = [i]

    part2 = countWeights(lines)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
