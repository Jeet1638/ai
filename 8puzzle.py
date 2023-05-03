def get_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return [i, j]

def get_child(puzzle):
    children = []
    blank = get_blank(puzzle)
    if blank[0] > 0:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[blank[0]][blank[1]], new_puzzle[blank[0] - 1][blank[1]] = \
            new_puzzle[blank[0] - 1][blank[1]], new_puzzle[blank[0]][blank[1]]
        children.append(new_puzzle)
    if blank[0] < 2:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[blank[0]][blank[1]], new_puzzle[blank[0] + 1][blank[1]] = \
            new_puzzle[blank[0] + 1][blank[1]], new_puzzle[blank[0]][blank[1]]
        children.append(new_puzzle)
    if blank[1] > 0:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[blank[0]][blank[1]], new_puzzle[blank[0]][blank[1] - 1] = \
            new_puzzle[blank[0]][blank[1] - 1], new_puzzle[blank[0]][blank[1]]
        children.append(new_puzzle)
    if blank[1] < 2:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[blank[0]][blank[1]], new_puzzle[blank[0]][blank[1] + 1] = \
            new_puzzle[blank[0]][blank[1] + 1], new_puzzle[blank[0]][blank[1]]
        children.append(new_puzzle)
    return children

def _8puzzle(start, goal):
    visited = []
    queue = []
    traversal_path = []
    visited.append(str(start))
    queue.append(str(start))
    while queue:
        current_node = eval(queue.pop(0))
        traversal_path.append(current_node)
        if current_node == goal:
            return traversal_path
        children = get_child(current_node)
        for child in children:
            child_string = str(child)
            if child_string not in visited:
                visited.append(child_string)
                queue.append(child_string)
    print("Solution doesn't exist!")


start = []
goal = []

print("Enter the start node:")
for i in range(3):
    row = list(map(int, input().split()))
    start.append(row)

print("Enter the goal node:")
for i in range(3):
    row = list(map(int, input().split()))
    goal.append(row)

for x in _8puzzle(start, goal):
    print(x)