def p2(grid):
    sum = 0
    for y in range(len(grid)):
        for x in range(len(grid)):
            sym = grid[y][x]
            if sym == "*":
                nums = []
                for dy, dx in [
                    (0, 1),
                    (1, 0),
                    (0, -1),
                    (-1, 0),
                    (1, 1),
                    (-1, -1),
                    (1, -1),
                    (-1, 1),
                ]:
                    yy = y + dy
                    xx = x + dx

                    if yy < len(grid) and xx < len(grid[yy]):
                        adj = grid[yy][xx]
                        
                        if adj.isdigit():
                            while xx - 1 >= 0 and grid[yy][xx - 1].isdigit():
                                xx -= 1

                            digits = []

                            while xx < len(grid[yy]) and grid[yy][xx].isdigit():
                                digits.append(grid[yy][xx])
                                grid[yy][xx] = "."
                                xx += 1

                            num = int("".join(digits))
                            nums.append(num)
                if len(nums) == 2: 
                    sum += nums[0] * nums[1]
                
    return sum
    


def p1(grid):
    sum = 0
    for y in range(len(grid)):
        for x in range(len(grid)):
            sym = grid[y][x]
            if sym != "." and not sym.isdigit():
                for dy, dx in [
                    (0, 1),
                    (1, 0),
                    (0, -1),
                    (-1, 0),
                    (1, 1),
                    (-1, -1),
                    (1, -1),
                    (-1, 1),
                ]:
                    yy = y + dy
                    xx = x + dx

                    if yy < len(grid) and xx < len(grid[yy]):
                        adj = grid[yy][xx]
                        if adj.isdigit():
                            while xx - 1 >= 0 and grid[yy][xx - 1].isdigit():
                                xx -= 1

                            digits = []

                            while xx < len(grid[yy]) and grid[yy][xx].isdigit():
                                digits.append(grid[yy][xx])
                                grid[yy][xx] = "."
                                xx += 1

                            num = int("".join(digits))
                            sum += num
    return sum


with open("input/03.txt") as f:
    print(p1([list(l) for l in f.readlines()]))
    f.seek(0)
    print(p2([list(l) for l in f.readlines()]))


