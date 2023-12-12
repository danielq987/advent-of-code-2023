from helpers import readFile

def main():
    lines = readFile("day12.txt")
    
    part1 = 0
    part2 = 0

    lookup = {}
    def solve(springs, numbers, index, new_group):
        """
        spring is a list of chars.
            it is updated to fill in the ? character with . or # as recursion happens
            otherwise, it is never modified
            
        numbers is the numbers array. modified on every loop to only contain the remaining unreached groups
            if spring (#): decrement numbers[0] by 1
            if broken (.) and spring[index] = 0: pop numbers[0]
        
        index is the current spring index we are at

        new_group is true if numbers[0] has not be decremented yet. else, false
        """
        spring_copy = springs.copy()
        nums = numbers.copy()

        n = len(nums)
        l = len(springs) 

        # key for memoization. keey track of the curre
        key = (numbers[0], n, index, new_group)
        
        # memo
        if key in lookup:
            return lookup[key]
        
        if not any(nums):
            # if there no numbers and no more springs, its a valid combo
            if "#" not in springs[index:]:
                return 1
            # if there are no numbers but still springs, its invalid
            return 0

        # ensure there are still enough springs available to fill the numbers/groups
        if (n - 1 + sum(nums) > l - index):
            return 0

        # make sure the current spring group does not exceed its target length
        if nums[0] == 0 and springs[index] == "#":
            return 0

        solutions = 0 
        
        # nums[0] == 0 means that the previous spring group just ended
        if nums[0] == 0:
            # this is the first "." broken spring after a working spring group
            spring_copy[index] = "."
            solutions += solve(spring_copy, nums[1:], index + 1, True)
        else:
            # this is a "." broken spring but not immediately after a valid group
            if springs[index] != "#" and new_group:
                spring_copy[index] = "."
                solutions += solve(spring_copy, nums, index + 1, True)

            # working spring
            if springs[index] != ".":
                spring_copy[index] = "#"
                nums[0] -= 1
                solutions += solve(spring_copy, nums, index + 1, False)

        # weird memo hack to make the code work :C
        if index > 20:
            lookup[key] = solutions

        return solutions
    
    for ind, line in enumerate(lines):
        springs, nums = line.split(" ")
        springs2 = [char for char  in ("?".join([springs]*5))]
        springs = [char for char in springs]
        nums = [int(num) for num  in nums.split(",")]
        nums2 = nums * 5
        
        c1 = solve(springs, nums, 0, True) 
        c2 = solve(springs2, nums2, 0, True) 
        part1 += c1
        part2 += c2
        
        lookup.clear()
         
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
