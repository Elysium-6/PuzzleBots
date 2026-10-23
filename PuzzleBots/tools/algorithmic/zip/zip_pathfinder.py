from tools.algorithmic.zip.map_cell import map_cell

zip_map = []
checkpoints = 0
solved_path = None

def initiate_map(n): # n = size, m = no of checkpoints
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(map_cell(False, False, False, False, 0))
        zip_map.append(temp)

def initiate_checkpoints():
    for i in range(int(input())):
        coords = input().split()
        zip_map[int(coords[0])][int(coords[1])].number = i + 1

def reset_map():
    for row in zip_map:
        for cell in row:
            cell.traversed = False

def show_map():
    for row in zip_map:
        for cell in row:
            if cell.traversed:
                print("X", end=" ")
            else:
                print(cell.number, end=" ")
        print()

def traverse(prev, path, i, j, n):
    global solved_path
    zip_map[i][j].traversed = True
    path.append([i, j])
    # print(prev, path, i, j, n)
    # print(f"Can down: {i < n - 1} Can right: {j < n - 1} Can up: {i > 0} Can left: {j > 0}")
    # show_map()
    if len(path) == n**2:
        # print("SOLVED")
        solved_path = list(path)

    if i < n-1:
        if  not zip_map[i+1][j].traversed:
            # print("down")
            if zip_map[i + 1][j].number == prev + 1:
                traverse(prev + 1, path, i + 1, j, n)
            elif zip_map[i + 1][j].number == 0:
                traverse(prev, path, i+1, j, n)
    if j < n-1:
        if not zip_map[i][j+1].traversed:
            # print("right")
            if zip_map[i][j+1].number == prev + 1:
                traverse(prev + 1, path, i, j + 1, n)
            elif zip_map[i][j+1].number == 0:
                traverse(prev, path, i, j+1, n)
    if i > 0:
        if not zip_map[i-1][j].traversed:
            # print("up")
            if zip_map[i - 1][j].number == prev + 1:
                traverse(prev + 1, path, i - 1, j, n)
            elif zip_map[i - 1][j].number == 0:
                traverse(prev, path, i - 1, j, n)
    if j > 0:
        if not zip_map[i][j-1].traversed:
            # print("left")
            if zip_map[i][j - 1].number == prev + 1:
                traverse(prev + 1, path, i, j - 1, n)
            elif zip_map[i][j - 1].number == 0:
                traverse(prev, path, i, j - 1, n)

    zip_map[i][j].traversed = False
    path.pop()

def solve_zip(i, j, n):
    traverse(1, [], i, j, n)

def main():
    initiate_map(int(input()))
    initiate_checkpoints()
    show_map()
    solve_zip(int(input()), int(input()), int(input()))
    print(solved_path)

main()