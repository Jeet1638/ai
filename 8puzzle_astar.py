import copy

def get_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return [i, j]

def get_child(puzzle):
    children = []
    blank = get_blank(puzzle)
    if blank[0] > 0:
        new_puzzle = copy.deepcopy(puzzle)
        new_puzzle[blank[0]][blank[1]], new_puzzle[blank[0] - 1][blank[1]] = \
            new_puzzle[blank[0] - 1][blank[1]], new_puzzle[blank[0]][blank[1]]
        children.append(new_puzzle)
    if blank[0] < 2:
        new_puzzle = copy.deepcopy(puzzle)
        new_puzzle[blank[0]][blank[1]], new_puzzle[blank[0] + 1][blank[1]] = \
            new_puzzle[blank[0] + 1][blank[1]], new_puzzle[blank[0]][blank[1]]
        children.append(new_puzzle)
    if blank[1] > 0:
        new_puzzle = copy.deepcopy(puzzle)
        new_puzzle[blank[0]][blank[1]], new_puzzle[blank[0]][blank[1] - 1] = \
            new_puzzle[blank[0]][blank[1] - 1], new_puzzle[blank[0]][blank[1]]
        children.append(new_puzzle)
    if blank[1] < 2:
        new_puzzle = copy.deepcopy(puzzle)
        new_puzzle[blank[0]][blank[1]], new_puzzle[blank[0]][blank[1] + 1] = \
            new_puzzle[blank[0]][blank[1] + 1], new_puzzle[blank[0]][blank[1]]
        children.append(new_puzzle)
    return children

def get_heuristic(puzzle, goal):
    h = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != goal[i][j]:
                h += 1
    return h

def _8puzzle(start, goal):
    traversal_path = []
    queue = [{'state': start, 'cost': 0, 'heuristic': get_heuristic(start, goal)}]
    visited = set()
    while queue:
        queue.sort(key=lambda x: x['cost'] + x['heuristic'])
        state = queue.pop(0)
        traversal_path.append(state['state'])
        if state['state'] == goal:
            return {'traversal_path': traversal_path, 'cost': state['cost']}
        visited.add(str(state['state']))
        children = get_child(state['state'])
        for child in children:
            child_cost = state['cost'] + 1
            child_heuristic = get_heuristic(child, goal)
            child_state = {'state': child, 'cost': child_cost, 'heuristic': child_heuristic}
            if str(child) not in visited:
                queue.append(child_state)
    return None

start = []
goal = []

print('Enter start state of the puzzle:')
for i in range(3):
    row = list(map(int, input().split()))
    start.append(row)

print('Enter goal state of the puzzle:')
for i in range(3):
    row = list(map(int, input().split()))
    goal.append(row)